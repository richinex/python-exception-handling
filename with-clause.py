try:
    with open('example.txt', 'r') as file:
        data = file.read()
        print(data)
except FileNotFoundError as e:
    print(f"File not found: {e}")
