def read_number():
    number = input("Enter a number: ")
    try:
        result = int(number)
    except ValueError:
        print("Not a valid number")
    else:
        print(f"The number is {result}")

read_number()
