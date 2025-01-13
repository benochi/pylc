import logging
from logging.handlers import RotatingFileHandler
from enum import Enum

# Define log levels
class LogLevel(Enum):
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL

class Logger:
    def __init__(self, file_name="app.log", max_bytes=1024 * 1024, backup_count=5):
        self.logger = logging.getLogger("AppLogger")
        self.logger.setLevel(logging.DEBUG)
        handler = RotatingFileHandler(file_name, maxBytes=max_bytes, backupCount=backup_count)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log(self, message, level):
        if level == LogLevel.DEBUG:
            self.logger.debug(message)
        elif level == LogLevel.INFO:
            self.logger.info(message)
        elif level == LogLevel.WARNING:
            self.logger.warning(message)
        elif level == LogLevel.ERROR:
            self.logger.error(message)
        elif level == LogLevel.CRITICAL:
            self.logger.critical(message)

    def set_log_level(self, level):
        self.logger.setLevel(level.value)
