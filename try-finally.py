def process_file(filename):
    f = open(filename, 'r')
    try:
        data = f.read()
        print(data)
    finally:
        f.close()
        print("File closed")

try:
    process_file("example.txt")
except FileNotFoundError as e:
    print(f"File not found: {e}")
