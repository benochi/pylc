import os
import json

class ConfigManager:
    def __init__(self):
        self.config = {}
        self.priority_sources = {}  # Track priorities for keys

    def load_config(self, source, priority=0):
        new_config = {}
        if source.endswith(".json"):
            if not os.path.exists(source):
                raise FileNotFoundError(f"Configuration file not found: {source}")
            with open(source, 'r', encoding='utf-8') as file:
                new_config = json.load(file)
        elif source == "env":
            new_config = dict(os.environ)
        else:
            raise ValueError(f"Unsupported config source: {source}")

        # Merge configurations based on priority
        for key, value in new_config.items():
            if key not in self.priority_sources or priority >= self.priority_sources[key]:
                self.config[key] = value
                self.priority_sources[key] = priority

    def get_config(self, key):
        return self.config.get(key)