class GardenError(Exception):
    """Eccezione base per tutti i problemi del giardino."""
    def __init__(self, message="Unknown garden error"):
        super().__init__(message)


class PlantError(GardenError):
    """Eccezione specifica per i problemi legati alle piante."""
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):
    """Eccezione specifica per i problemi legati all'irrigazione."""
    def __init__(self, message="Unknown water error"):
        super().__init__(message)


def check_plant_health(is_wilting):
    """Lancia PlantError se la pianta sta appassendo."""
    if is_wilting:
        raise PlantError("The tomato plant is wilting!")


def check_water_level(water_liters):
    """Lancia WaterError se l'acqua è insufficiente."""
    if water_liters < 10:
        raise WaterError("Not enough water in the tank!")


def test_custom_errors():
    print("=== Custom Garden Errors Demo ===")
    print("\n")
    print("Testing PlantError...")
    try:
        check_plant_health(is_wilting=True)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print("\n")
    print("Testing WaterError...")
    try:
        check_water_level(water_liters=2)
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print("\n")
    print("Testing catching all garden errors...")
    actions = [
        lambda: check_plant_health(is_wilting=True),
        lambda: check_water_level(water_liters=2)
        ]
    i = 0
    while i < len(actions):
        try:
            actions[i]()
        except GardenError as e:
            # Cattura sia PlantError che WaterError grazie all'ereditarietà
            print(f"Caught GardenError: {e}")
        i += 1
    print("\n")
    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
