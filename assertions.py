def divide(x, y):
    assert y != 0, "y cannot be zero"
    return x / y

try:
    result = divide(10, 0)
except AssertionError as e:
    print(f"Assertion error: {e}")
