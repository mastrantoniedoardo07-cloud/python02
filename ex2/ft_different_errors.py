def garden_operations(operation_number):
        if operation_number == 0:
            int("abc")
        elif operation_number == 1:
            1 / 0
        elif operation_number == 2:
            open("non_existent_file.txt", "r")
        elif operation_number == 3:
            "Garden" + 42
        else:
            return


def test_error_types():
    print("=== Testing Individual Exception Handling ===")

    # Test 1: Gestione con except singoli usando un ciclo while
    op = 0
    while op < 4:
        print(f"\nTesting operation_number = {op}:")
        try:
            garden_operations(op)
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")
        
        op += 1  # Incremento per l'iterazione successiva

    print("\n" + "=" * 45)
    print("=== Testing Multiple Exceptions in One Block ===")

    # Test 2: Gestione con cattura multipla (tupla) usando un altro ciclo while
    op = 0
    while op < 4:
        print(f"\nTesting operation_number = {op} (multiple catch):")
        try:
            garden_operations(op)
        except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError) as e:
            print(f"Caught an expected error ({type(e).__name__}): {e}")
        
        op += 1  # Incremento per l'iterazione successiva

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_error_types()