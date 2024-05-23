try:
    x = [1, 2, 3]
    print(x[5])
except IndexError as e:
    print(f"Index error: {e}")
except Exception as e:
    print(f"General error: {e}")
