# 4. Preserving the Original Traceback

# When you re-raise an exception, the original traceback is preserved, which is helpful
# for debugging because it shows where the exception originally occurred.
def risky_operation():
    try:
        raise ValueError("An error occurred")
    except ValueError as e:
        print(f"Logging the error: {e}")
        raise  # Re-raise to keep the original traceback

def main():
    try:
        risky_operation()
    except ValueError as e:
        print(f"Handling error in main: {e}")

if __name__ == "__main__":
    main()


# Add additional logging or context to the exception.
# Perform cleanup operations before allowing the exception to propagate.
# Partially handle the exception but still propagate it for further handling.
# Preserve the original traceback for better debugging and error reporting.