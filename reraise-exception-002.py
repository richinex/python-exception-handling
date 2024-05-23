# 1. Adding Context or Logging Additional Information

# In some cases, you might want to catch an exception to log some additional information
# or add context before re-raising it for further handling.

import logging

def process_data(data):
    try:
        result = 10 / data
    except ZeroDivisionError as e:
        logging.error(f"Error processing data: {data}, error: {e}")
        raise  # Re-raise the exception after logging

def main():
    try:
        process_data(0)
    except ZeroDivisionError as e:
        print(f"Handling the exception at a higher level: {e}")

if __name__ == "__main__":
    main()
