try:
    try:
        x = 10 / 0
    except ZeroDivisionError:
        print("Inner exception caught")
        raise
except ZeroDivisionError:
    print("Outer exception caught")
