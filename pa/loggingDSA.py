import os

LOG_LEVELS = {
    "DEBUG": "DEBUG",
    "INFO": "INFO",
    "WARNING": "WARNING",
    "ERROR": "ERROR",
    "CRITICAL": "CRITICAL"
}

class Logger:
    def __init__(self, file_name="app.log", max_bytes=1024 * 1024, backup_count=5):
        self.file_name = file_name
        self.max_bytes = max_bytes
        self.backup_count = backup_count

    def _rotate_logs(self):
        """
        Rotate log files when the size limit is reached.
        """
        if os.path.exists(self.file_name) and os.path.getsize(self.file_name) > self.max_bytes:
            # Rotate logs manually
            for i in range(self.backup_count - 1, 0, -1):
                old_file = f"{self.file_name}.{i}"
                new_file = f"{self.file_name}.{i + 1}"
                if os.path.exists(old_file):
                    os.rename(old_file, new_file)

            # Rename the current log file
            os.rename(self.file_name, f"{self.file_name}.1")

    def log(self, message, level):
        """
        Write a log message with the specified log level to the file.
        """
        if level not in LOG_LEVELS:
            raise ValueError(f"Invalid log level: {level}")

        log_entry = f"{LOG_LEVELS[level]} - {message}\n"

        # Check if log rotation is needed
        self._rotate_logs()

        # Append the log entry to the file
        with open(self.file_name, "a", encoding="utf-8") as log_file:
            log_file.write(log_entry)
