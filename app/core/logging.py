"""
This module contains the configuration for the logging system.
"""

import sys
import logging
import structlog

from structlog.processors import add_log_level, TimeStamper, format_exc_info, KeyValueRenderer


class SafeFileHandler(logging.FileHandler):
    def emit(self, record):
        if self.stream and not self.stream.closed:
            try:
                super().emit(record)
            except NotImplementedError:
                self.handleError(record)


class StreamToLogger:
    """
    Custom stream to redirect stdout and stderr to the logger
    """
    def __init__(self, logger_instance, log_level=logging.INFO):
        """
        Initialize the stream

        :param logger:
        :param log_level:
        """
        self.logger = logger_instance
        self.log_level = log_level
        self.line_buffer = ""

    def write(self, buf):
        """
        Write the buffer to the stream

        :param buf:
        :return:
        """
        for line in buf.rstrip().splitlines():
            if isinstance(line, bytes):
                line = line.decode("utf-8")

            if "Waiting to be ready..." in line:
                continue

            if "ERROR" == line:
                continue

            self.logger.log(self.log_level, line.rstrip())

    def flush(self):
        """
        Flush the stream

        :return:
        """

    def isatty(self):
        """
        Check if the stream is a tty

        :return:
        """
        return False


# Configure logging
logging.basicConfig(level=logging.INFO, format="[%(asctime)s] [%(levelname)s] %(message)s")
structlog.configure(
    processors=[
        structlog.contextvars.merge_contextvars,
        structlog.processors.StackInfoRenderer(),
        structlog.dev.set_exc_info,
        add_log_level,
        format_exc_info,
        TimeStamper(fmt="iso", utc=False),
        KeyValueRenderer(key_order=["timestamp", "level", "event"]),
    ],
    context_class=dict,
    logger_factory=structlog.stdlib.LoggerFactory(),
    wrapper_class=structlog.stdlib.BoundLogger,
    cache_logger_on_first_use=True,
)

# Redirect stdout and stderr to the logger
stdout_logger = logging.getLogger('STDOUT')
stderr_logger = logging.getLogger('STDERR')

sys.stdout = StreamToLogger(stdout_logger, logging.INFO)
sys.stderr = StreamToLogger(stderr_logger, logging.ERROR)

# Add the custom SafeFileHandler
file_handler = SafeFileHandler("app.log")
logger = structlog.get_logger(name="demo")
logger.addHandler(file_handler)
