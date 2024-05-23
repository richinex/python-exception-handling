class CustomError(Exception):
    pass

def raise_custom_error():
    raise CustomError("This is a custom error")

try:
    raise_custom_error()
except CustomError as e:
    print(f"Caught an error: {e}")
