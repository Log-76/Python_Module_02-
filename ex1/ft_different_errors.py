def garden_operations(temp_str):
    try:
        temp = int(temp_str)
        temp = 5 / temp
        temp = open(temp_str)
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
    except KeyError:
        print("Caught KeyError: 'missing\_plant'")


def test_error_types():
    print("=== Garden Error Types Demo ===")
    print()
    print("Testing ValueError...")
    garden_operations("abc")
    print()
    print("Testing ZeroDivisionError...")
    garden_operations(0)
    print()
    print("Testing ZeroDivisionError...")
    garden_operations("")


test_error_types()