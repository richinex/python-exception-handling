try:
    x = 10 / 0
except ZeroDivisionError as e:
    print(f"Caught an error: {e}")
    raise  # Re-raise the exception
