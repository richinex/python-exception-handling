class ManagedResource:
    def __enter__(self):
        print("Resource acquired")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            print(f"Exception occurred: {exc_value}")
        print("Resource released")
        return True  # Suppress exception

with ManagedResource():
    raise ValueError("An error occurred")
