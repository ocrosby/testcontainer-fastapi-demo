"""
This module contains the configuration for the logging system.
"""

import logging
import structlog

# Configure logging
logging.basicConfig(level=logging.INFO, format="[%(asctime)s] [%(levelname)s] %(message)s")
structlog.configure(
    processors=[
        structlog.contextvars.merge_contextvars,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
        # structlog.dev.set_exc_info,
        structlog.processors.TimeStamper(fmt="iso", utc=False),
        # structlog.processors.add_log_level,
        structlog.dev.ConsoleRenderer(),
        # structlog.processors.JSONRenderer(),
    ],
    wrapper_class=structlog.make_filtering_bound_logger(logging.NOTSET),
    context_class=dict,
    logger_factory=structlog.stdlib.LoggerFactory(),
    cache_logger_on_first_use=False,
)

logger = structlog.get_logger(name="demo")
