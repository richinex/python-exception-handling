try:
    x = int("hello")
except (ValueError, TypeError) as e:
    print(f"An error occurred: {e}")
