import logging
from logging.handlers import RotatingFileHandler

class Logger:
    def __init__(self, file_name="app.log", backup_count=5, log_level="INFO"):
        self.logger = logging.getLogger("AppLogger")
        self.logger.setLevel(log_level)

        # Rotating file handler with fixed number of backups
        handler = RotatingFileHandler(
            file_name,
            backupCount=backup_count
        )
        self.logger.addHandler(handler)

    def set_log_level(self, level):
        if level not in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
            raise ValueError(f"Invalid log level: {level}")
        self.logger.setLevel(level)

    def log(self, message, level="INFO"):
        if level == "DEBUG":
            self.logger.debug(message)
        elif level == "INFO":
            self.logger.info(message)
        elif level == "WARNING":
            self.logger.warning(message)
        elif level == "ERROR":
            self.logger.error(message)
        elif level == "CRITICAL":
            self.logger.critical(message)
        else:
            raise ValueError(f"Invalid log level: {level}")
