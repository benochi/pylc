import os
import logging

# Custom exceptions
class FileProcessingError(Exception):
    pass

class FileNotFoundError(FileProcessingError):
    pass

class InvalidFileFormatError(FileProcessingError):
    pass

class FileProcessor:
    def __init__(self, log_file="app.log"):
        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,
        )

    def process_file(self, file_path):
        try:
            # Check if the file exists
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"File not found: {file_path}")

            # Simulate file processing
            with open(file_path, "r", encoding="utf-8") as file:
                for line in file:
                    if not line.strip():
                    # fields = line.strip().split(",")  # Assuming CSV format
                    # if len(fields) < 3:
                        raise InvalidFileFormatError(f"Invalid line in file: {file_path}")

            # Log success
            logging.info(f"File processed successfully: {file_path}")

        except FileNotFoundError as e:
            logging.error(f"Error: {e}")
            raise
        except InvalidFileFormatError as e:
            logging.error(f"Error: {e}")
            raise
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            raise FileProcessingError(f"Unexpected error processing file: {e}")
