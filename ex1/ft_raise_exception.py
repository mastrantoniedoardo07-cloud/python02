def input_temperature(temp_str):
    try:
        temperature = int(temp_str)
        if temperature > 40:
            raise ValueError(f"{temperature}°C is too hot for plants (max 40°C)")
        if temperature < 0:
            raise ValueError(f"{temperature}°C is too cold for plants (min 0°C)")
        print(f"Temperature is now {temperature}°C")
        return temperature

    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
        return None


def test_temperature():
    print("=== Garden Temperature Checker ===")
    tests = ["25", "abc", "100", "-50"]
    for t in tests:
        print("\n")
        print(f"Input data is '{t}'")
        input_temperature(t)
    print("\n")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()