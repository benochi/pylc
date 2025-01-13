import logging

# Custom exception types
class FileProcessingError(Exception):
    pass

class FileNotFoundError(FileProcessingError):
    pass

class InvalidFileFormatError(FileProcessingError):
    pass

def process_file(file_path):
    try:
        # Check if the file exists
        with open(file_path, 'r', encoding='utf-8') as file:
            # Simulate file processing
            for line in file:
                if not line.strip():
                    raise InvalidFileFormatError(f"Invalid line found in file: {file_path}")
            logging.info(f"File processed successfully: {file_path}")
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        raise FileNotFoundError(f"File not found: {file_path}")
    except InvalidFileFormatError as e:
        logging.error(str(e))
        raise
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise FileProcessingError("An unexpected error occurred during file processing.") from e