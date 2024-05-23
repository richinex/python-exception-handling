class CustomError(Exception):
    pass

class SpecificError(CustomError):
    pass

try:
    raise SpecificError("This is a specific custom error")
except CustomError as e:
    print(f"Caught an error: {e}")
