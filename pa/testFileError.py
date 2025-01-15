from fileError import FileProcessor, FileProcessingError, FileNotFoundError, InvalidFileFormatError

def test_file_processor():
    processor = FileProcessor()

    # Test case 1: Valid file
    try:
        processor.process_file("valid.txt")
        print("Test case 1 passed: Valid file processed successfully.")
    except Exception as e:
        print(f"Test case 1 failed: {e}")

    # Test case 2: File not found
    try:
        processor.process_file("nonexistent.txt")
        print("Test case 2 failed: Non-existent file should raise an exception.")
    except FileNotFoundError:
        print("Test case 2 passed: FileNotFoundError raised for non-existent file.")
    except Exception as e:
        print(f"Test case 2 failed: Unexpected exception {e}")

    # Test case 3: File with invalid format
    try:
        processor.process_file("invalid_format.txt")
        print("Test case 3 failed: Invalid file format should raise an exception.")
    except InvalidFileFormatError:
        print("Test case 3 passed: InvalidFileFormatError raised for invalid format.")
    except Exception as e:
        print(f"Test case 3 failed: Unexpected exception {e}")

    # Test case 4: Unexpected error (optional, if you want to test general exception handling)
    try:
        processor.process_file(None)  # Passing None should cause an unexpected error
        print("Test case 4 failed: Unexpected input should raise an exception.")
    except FileProcessingError:
        print("Test case 4 passed: FileProcessingError raised for unexpected input.")
    except Exception as e:
        print(f"Test case 4 failed: Unexpected exception {e}")

if __name__ == "__main__":
    test_file_processor()
