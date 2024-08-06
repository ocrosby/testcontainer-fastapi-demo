"""
This module contains the configuration for the logging system.
"""

import logging
import structlog


class SafeFileHandler(logging.FileHandler):
    def emit(self, record):
        if self.stream and not self.stream.closed:
            try:
                super().emit(record)
            except Exception:
                self.handleError(record)
        else:
            logging.warning(f"Attempt to write to a closed file.")


# Configure logging
logging.basicConfig(level=logging.INFO, format="[%(asctime)s] [%(levelname)s] %(message)s")
structlog.configure(
    processors=[
        structlog.processors.KeyValueRenderer(key_order=["timestamp", "level", "event", "logger"]),
        # structlog.contextvars.merge_contextvars,
        # structlog.processors.TimeStamper(fmt="iso"),
        # structlog.processors.StackInfoRenderer(),
        # structlog.dev.set_exc_info,
        # structlog.processors.TimeStamper(fmt="iso", utc=False),
        # structlog.processors.add_log_level,
        # structlog.dev.ConsoleRenderer(),
        # structlog.processors.JSONRenderer(),
    ],
    # wrapper_class=structlog.make_filtering_bound_logger(logging.NOTSET),
    context_class=dict,
    logger_factory=structlog.stdlib.LoggerFactory(),
    wrapper_class=structlog.stdlib.BoundLogger,
    cache_logger_on_first_use=True,
)

# Add the custom SafeFileHandler
file_handler = SafeFileHandler("app.log")
logger = structlog.get_logger(name="demo")
logger.addHandler(file_handler)
