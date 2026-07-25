def input_temperature(temp_str):
    try:
        temperature = int(temp_str)
        print(f"Temperature is now {temperature}°C")
        return temperature
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
        return None
    


def test_temperature():
    print("=== Garden Temperature ===")
    t = "25"
    print(f"Input data is {t}")
    input_temperature(t)
    print()
    str = "abc"
    print(f"Input data is  {str}")
    input_temperature(str)
    print()
    return(print("All tests completed - program didn't crash!"))


if __name__ == "__main__":
    test_temperature()