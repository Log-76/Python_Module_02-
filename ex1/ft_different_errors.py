def garden_operations(temp_str):
    try:
        temp = int(temp_str)
        temp = 5 / temp
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
