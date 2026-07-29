class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, plant_name: str) -> None:
        msg = f"Caught PlantError: Invalid plant name to water: '{plant_name}'"
        super().__init__(msg)


def water_plant(plant_name: str) -> None:
    try:
        if plant_name != str.capitalize(plant_name):
            raise PlantError(plant_name)
        print(f"Watering {plant_name}: [OK]")
    except PlantError as e:
        raise e


def test_watering_system() -> None:
    print("=== Garden Watering System ===")
    print("")
    print("Testing valid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrots")
    except PlantError as e:
        print(e)
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")
    print("")
    print("Testing invalid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("lettuce")
        water_plant("Carrots")
    except PlantError as e:
        print(e)
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


def main() -> None:
    test_watering_system()
    print("")
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
