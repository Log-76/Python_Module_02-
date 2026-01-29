class GardenManager:
    def __init__(self, name, water_tank):
        self.name = name
        self.water_tank = int(water_tank)
        self.garden = []

    def add(self, plante):
        try:
            plant_verif(plante.name)
            self.garden.append(plante)
            print(f"Added {plante.name}  successfully")
        except PlantError:
            print("Error adding plant: Plant name cannot be empty!")

    def water_plants(self):
        print("Opening watering system")
        try:
            for plant in self.garden:
                print(f"Watering {plant} success")
        finally:
            print("Closing watering system (cleanup)")

    def plant_health(self):
        try:
            for plant in self.garden:
                check_plant_health(plant.water, plant.sunligth)
                print(f"{plant.name}: healthy (water:{plant.water}, "
                      f"sun: {plant.sunligth})")
        except WaterError as e:
            print(e)
        except SunlightError as e:
            print(e)

    def Tank(self):
        try:
            verif_erreur(self.water_tank)
        except GardenError as e:
            print(e)
        finally:
            print("System recovered and continuing...")


class SunlightError(Exception):
    def __init__(self, sunlight):
        self.sunlight = int(sunlight)
        if self.sunlight > 10:
            super().__init__(f"Error: Sunlight hours {sunlight}"
                             f" is too high (max 12)")
        else:
            super().__init__(f"Error: Sunlight hours {sunlight} "
                             f"is too low (min 2)")


class WaterError(Exception):
    def __init__(self, water):
        self.water = int(water)
        if self.water > 10:
            super().__init__(f"Error: Water level {water}"
                             f" is too high (max 10)")
        elif self.water < 1:
            super().__init__(f"Error: Water level {water}"
                             f" is too low (min 1)")


def check_plant_health(water_level, sunlight_hours):
    if water_level < 1 or water_level > 10:
        raise WaterError(water_level)
    if sunlight_hours < 2 or sunlight_hours > 12:
        raise SunlightError(sunlight_hours)


class PlantError(Exception):
    def __init__(self, name):
        self.name = name


def plant_verif(plant):
    if not isinstance(plant, str) or plant == "":
        raise PlantError(plant)


class GardenError(Exception):
    def __init__(self, water_tank):
        self.water_tank = water_tank
        super().__init__("Caught GardenError: Not enough water in tank")


def verif_erreur(water_tank):
    if water_tank == 0:
        raise GardenError(water_tank)


class Plant:
    def __init__(self, name, sunligth, water):
        self.name = name
        self.sunligth = sunligth
        self.water = water

    def __str__(self):
        return f"{self.name}"


def test_garden_management():
    tomate = Plant("Tomate", 2, 2)
    lettuce = Plant("lettuce", 85, 1)
    empty = Plant("", 2, 15)
    alice = GardenManager("alice", 0)
    print("=== Garden Management System ===")
    print()
    print("Adding plants to garden...")
    alice.add(tomate)
    alice.add(lettuce)
    alice.add(empty)
    print()
    print("Watering plants...")
    alice.water_plants()
    print()
    print("Checking plant health...")
    alice.plant_health()
    print()
    print("Testing error recovery...")
    alice.Tank()


# test_garden_management()
