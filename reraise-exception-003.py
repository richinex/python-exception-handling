# 2. Cleanup Operations Before Re-Raising

# If you need to perform some cleanup operations (like closing files or releasing resources)
# before re-raising the exception, you can do this in the except block.

def read_file(file_path):
    try:
        f = open(file_path, 'r')
        data = f.read()
        return data
    except FileNotFoundError as e:
        print(f"File not found: {file_path}")
        raise  # Re-raise the exception
    finally:
        try:
            f.close()
        except NameError:
            pass

def main():
    try:
        content = read_file("non_existent_file.txt")
    except FileNotFoundError as e:
        print(f"Handling file not found at a higher level: {e}")

if __name__ == "__main__":
    main()
