class NameError(Exception):
    def __init__(self, name: str):
        self.name = name
        super().__init__("Error:nom manquant")


class WaterError(Exception):
    def __init__(self, water: int):
        self.water = int(water)
        if self.water > 10:
            super().__init__(f"Error: Water level {water}"
                             f" is too high (max 10)")
        elif self.water < 1:
            super().__init__(f"Error: Water level {water}"
                             f" is too low (min 1)")


class SunlightError(Exception):
    def __init__(self, sunlight: int):
        self.sunlight = int(sunlight)
        if self.sunlight > 10:
            super().__init__(f"Error: Sunlight hours {sunlight}"
                             f" is too high (max 12)")
        else:
            super().__init__(f"Error: Sunlight hours {sunlight} "
                             f"is too low (min 2)")


def check_plant_health(plant_name: str, water_level: int, sunlight_hours: int):
    if not plant_name:
        raise NameError(plant_name)
    if water_level < 1 or water_level > 10:
        raise WaterError(water_level)
    if sunlight_hours < 2 or sunlight_hours > 12:
        raise SunlightError(sunlight_hours)
    print(f"{plant_name} is healthy!")


def test_plant_checks():
    print("=== Garden Plant Health Checker ===")
    print()
    print("Testing good values...")
    try:
        check_plant_health("tomate", 5, 5)
    except NameError as e:
        print(e)
    except WaterError as e:
        print(e)
    except SunlightError as e:
        print(e)
    print()
    print("Testing empty plant name...")
    try:
        check_plant_health("", 5, 5)
    except NameError as e:
        print(e)
    except WaterError as e:
        print(e)
    except SunlightError as e:
        print(e)
    print()
    print("Testing bad water level...")
    try:
        check_plant_health("Tomate", 15, 5)
    except NameError as e:
        print(e)
    except WaterError as e:
        print(e)
    except SunlightError as e:
        print(e)
    print()
    print("Testing bad sunlight hours...")
    try:
        check_plant_health("Tomate", 5, 0)
    except NameError as e:
        print(e)
    except WaterError as e:
        print(e)
    except SunlightError as e:
        print(e)
    print()
    print("All error raising tests completed!")


# test_plant_checks()
