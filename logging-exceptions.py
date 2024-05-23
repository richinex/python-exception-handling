import logging

logging.basicConfig(level=logging.ERROR)

try:
    x = 10 / 0
except ZeroDivisionError as e:
    logging.error(f"An error occurred: {e}", exc_info=True)
