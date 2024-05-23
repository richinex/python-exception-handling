# 3. Partial Handling of Exceptions

# Sometimes, you might want to handle part of an exception
# (e.g., logging it) but still allow it to propagate up the call stack for further handling or logging.
def perform_calculation(x):
    try:
        result = 10 / x
    except ZeroDivisionError as e:
        print(f"Division by zero encountered: {e}")
        raise  # Re-raise the exception

def main():
    try:
        perform_calculation(0)
    except ZeroDivisionError as e:
        print(f"Caught an error in main: {e}")

if __name__ == "__main__":
    main()
