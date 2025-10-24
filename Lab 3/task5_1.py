def convert_temperature():
    """
    Converts temperature between Celsius, Fahrenheit, and Kelvin.
    Provides clear instructions to the user.
    """
    print("Welcome to the Temperature Converter!")
    print("You can convert temperatures between Celsius, Fahrenheit, and Kelvin.")
    print("Please follow the instructions below.")

    print("\nTemperature scales:")
    print("1. Celsius (C)")
    print("2. Fahrenheit (F)")
    print("3. Kelvin (K)")

    scale_from = input("Enter the number corresponding to the scale you want to convert FROM (1/2/3): ").strip()
    scale_to = input("Enter the number corresponding to the scale you want to convert TO (1/2/3): ").strip()

    scale_dict = {'1': 'Celsius', '2': 'Fahrenheit', '3': 'Kelvin'}

    if scale_from not in scale_dict or scale_to not in scale_dict:
        print("Invalid scale selection. Please enter 1, 2, or 3.")
        return

    try:
        temp = float(input(f"Enter the temperature value in {scale_dict[scale_from]}: "))
    except ValueError:
        print("Invalid temperature value. Please enter a numeric value.")
        return

    def celsius_to_fahrenheit(c):
        return c * 9/5 + 32

    def celsius_to_kelvin(c):
        return c + 273.15

    def fahrenheit_to_celsius(f):
        return (f - 32) * 5/9

    def fahrenheit_to_kelvin(f):
        return (f - 32) * 5/9 + 273.15

    def kelvin_to_celsius(k):
        return k - 273.15

    def kelvin_to_fahrenheit(k):
        return (k - 273.15) * 9/5 + 32

    result = None

    if scale_from == scale_to:
        result = temp
    elif scale_from == '1' and scale_to == '2':
        result = celsius_to_fahrenheit(temp)
    elif scale_from == '1' and scale_to == '3':
        result = celsius_to_kelvin(temp)
    elif scale_from == '2' and scale_to == '1':
        result = fahrenheit_to_celsius(temp)
    elif scale_from == '2' and scale_to == '3':
        result = fahrenheit_to_kelvin(temp)
    elif scale_from == '3' and scale_to == '1':
        result = kelvin_to_celsius(temp)
    elif scale_from == '3' and scale_to == '2':
        result = kelvin_to_fahrenheit(temp)

    print(f"\n{temp} {scale_dict[scale_from]} is equal to {result:.2f} {scale_dict[scale_to]}.")

# Example usage:
convert_temperature()
