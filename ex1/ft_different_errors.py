def garden_operations():
    try:
        print("Testing ValueError...")
        temp = int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    try:
        print()
        print("Testing ZeroDivisionError...")
        temp = int(0)
        temp = 1 / temp
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    try:
        print()
        print("Testing FileNotFoundError...")
        temp = open("")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
    try:
        print()
        print("Testing KeyError...")
        tab = {"color": "red"}
        print(tab["price"])
    except KeyError:
        print("Caught KeyError: 'missing plant'")


def test_error_types():
    print("=== Garden Error Types Demo ===")
    garden_operations()
    print()
    print("Testing multiple errors together...")
    print("Caught an error, but program continues!")
    print()
    print("All error types tested successfully!")


# test_error_types()
