def check_temperature(temp_str: int) -> int:
    print(f"Testing temperature: {temp_str}")
    try:
        temp = int(temp_str)
    except ValueError:
        print(f"Error: {temp_str} is not a valid number")
        return
    if temp >= 0 and temp <= 40:
        print(f"Temperature {temp}°C is perfect for plants!")
        return temp
    elif temp > 40:
        print(f"Error: {temp}°C is too hot for plants (max 40°C)")
        return
    elif temp < 0:
        print(f"Error: {temp}°C is too cold for plants (min 0°C)")


def test_temperature_input():
    print("=== Garden Temperature Checker ===")
    print()
    check_temperature(25)
    print()
    check_temperature("abc")
    print()
    check_temperature(100)
    print()
    check_temperature(-50)
    print()
    print("All tests completed - program didn't crash!")


# test_temperature_input()
