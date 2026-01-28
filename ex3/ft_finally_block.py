class PlantError(Exception):
    def __init__(self, name):
        self.name = name


def plant_verif(plant):
    if not isinstance(plant, str):
        raise PlantError(plant)


def water_plants(plant_list):
    print("Opening watering system")
    try:
        for plant in plant_list:
            plant_verif(plant)
            print(f"Watering {plant}")
    except PlantError:
        print("Error: Cannot water None - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    print("=== Garden Watering System ===")
    print()
    tab = ["Tomato", "lettuce", "carrots"]
    water_plants(tab)
    print()
    tab2 = ["Tomato", 102, "carrots"]
    water_plants(tab2)


# test_watering_system()
