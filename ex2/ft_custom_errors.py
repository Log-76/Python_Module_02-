class GardenError(Exception):
    pass


"""
PlantError(GardenError): est une classe qui herite de GardenError
le init pour faire de la gestion d erreur qui permet recuperer
les info obligatoire et print l erreur avec un message
"""


class PlantError(GardenError):
    def __init__(self, name: str, water: int):
        self.water = int(water)
        print(f"Caught PlantError: The {name} plant is wilting!")


class WaterError(PlantError):
    def __init__(self, water_tank: int):
        self.water_tank = int(water_tank)
        print("Caught WaterError: Not enough water in the tank!")


"""
def verif_erreur(water_tank): et def verif_plant(name, water):
permet de via les info donner verifier si on est dans un cas d erreur
via un if fait appel a la fonction de verif raise
raise : Stop tout ! Il y a un problème ! donc il passe a la suite
du programme sans continiuer le try
"""


def verif_erreur(water_tank: int):
    if water_tank == 0:
        raise WaterError(water_tank)


def verif_plant(name: str, water: int):
    if water > 2:
        raise PlantError(name, water)


def test_error_types():
    print("=== Custom Garden Errors Demo ===")
    print()
    print("Testing PlantError...")
    try:
        verif_plant("Tomate", 3)
    except PlantError:
        print()
    print("Testing WaterError...")
    try:
        verif_erreur(0)
    except WaterError:
        print()
    print("Testing catching all garden errors...")
    try:
        verif_plant("Tomate", 3)
    except PlantError:
        try:
            verif_erreur(0)
        except WaterError:
            print()


test_error_types()
