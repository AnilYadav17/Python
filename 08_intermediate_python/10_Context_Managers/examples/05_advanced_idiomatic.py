"""
05_advanced_idiomatic.py
Demonstrates dual-purpose context manager and decorator using contextlib.ContextDecorator:
- Implements TemporaryEnvironment to safely mutate os.environ
- Usable as BOTH 'with TemporaryEnvironment(...):' AND '@TemporaryEnvironment(...)'
"""

import os
from contextlib import ContextDecorator

class TemporaryEnvironment(ContextDecorator):
    """
    Context manager and decorator that temporarily sets environment variables
    and restores the original values upon exit.
    """
    def __init__(self, **env_overrides):
        self.overrides = env_overrides
        self.originals = {}

    def __enter__(self):
        for key, value in self.overrides.items():
            self.originals[key] = os.environ.get(key)
            os.environ[key] = str(value)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        for key, original_value in self.originals.items():
            if original_value is None:
                # Key did not exist originally -> delete it
                os.environ.pop(key, None)
            else:
                # Key existed originally -> restore original value
                os.environ[key] = original_value
        return False  # Do not suppress exceptions


# Usage 1: Used as a function decorator via ContextDecorator
@TemporaryEnvironment(APP_STAGE="STAGING", LOG_LEVEL="DEBUG")
def execute_staged_task():
    print(f"  Inside decorated function -> APP_STAGE: '{os.environ.get('APP_STAGE')}', LOG_LEVEL: '{os.environ.get('LOG_LEVEL')}'")


def main():
    print("--- 1. Using TemporaryEnvironment as Context Manager ---")
    os.environ["API_KEY"] = "PRODUCTION_KEY_ORIGINAL"
    print(f"Initial API_KEY: {os.environ.get('API_KEY')}")

    with TemporaryEnvironment(API_KEY="MOCK_TESTING_KEY", NEW_SETTING="ENABLED"):
        print(f"  Inside with block -> API_KEY: {os.environ.get('API_KEY')}")
        print(f"  Inside with block -> NEW_SETTING: {os.environ.get('NEW_SETTING')}")

    print(f"Restored API_KEY outside block: {os.environ.get('API_KEY')}")
    print(f"Restored NEW_SETTING outside block: {os.environ.get('NEW_SETTING')}")

    print("\n--- 2. Using TemporaryEnvironment as Function Decorator ---")
    execute_staged_task()
    print(f"Outside decorated function -> APP_STAGE: '{os.environ.get('APP_STAGE')}' (Cleanly restored!)")

if __name__ == "__main__":
    main()
