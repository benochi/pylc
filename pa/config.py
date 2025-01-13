import os
import json

class ConfigManager:
    def __init__(self):
        self.config = {}

    def load_config(self, source):
        if source.endswith(".json"):
            with open(source, 'r', encoding='utf-8') as file:
                self.config.update(json.load(file))
        elif source == "env":
            self.config.update(os.environ)
        else:
            raise ValueError(f"Unsupported config source: {source}")

    def get_config(self, key):
        return self.config.get(key)

# Usage example
if __name__ == "__main__":
    # Error Handling Example
    try:
        process_file("sample.txt")
    except FileProcessingError as e:
        print(f"Error: {e}")

    # Logging Example
    logger = Logger()
    logger.set_log_level(LogLevel.INFO)
    logger.log("Application started", LogLevel.INFO)

    # Configuration Management Example
    config_manager = ConfigManager()
    config_manager.load_config("config.json")  # Assuming a JSON file
    config_manager.load_config("env")  # Load environment variables
    print(config_manager.get_config("APP_NAME"))
