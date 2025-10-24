def improved_temperature_converter():
    """
    Improved temperature conversion tool with clear instructions and weather condition advice.
    Allows user to convert between Celsius, Fahrenheit, and Kelvin.
    Also provides a simple weather condition based on the converted temperature.
    """
    print("Welcome to the Improved Temperature Converter!")
    print("You can convert temperatures between Celsius, Fahrenheit, and Kelvin.")
    print("Select the scale you want to convert FROM and TO:")
    print("1. Celsius (°C)")
    print("2. Fahrenheit (°F)")
    print("3. Kelvin (K)")

    scale_dict = {'1': 'Celsius', '2': 'Fahrenheit', '3': 'Kelvin'}

    scale_from = input("Enter the number for the scale to convert FROM (1/2/3): ").strip()
    scale_to = input("Enter the number for the scale to convert TO (1/2/3): ").strip()

    if scale_from not in scale_dict or scale_to not in scale_dict:
        print("Invalid scale selection. Please enter 1, 2, or 3.")
        return

    try:
        temp = float(input(f"Enter the temperature value in {scale_dict[scale_from]}: "))
    except ValueError:
        print("Invalid temperature value. Please enter a numeric value.")
        return

    # Conversion functions
    def to_celsius(value, from_scale):
        if from_scale == '1':  # Celsius
            return value
        elif from_scale == '2':  # Fahrenheit
            return (value - 32) * 5/9
        elif from_scale == '3':  # Kelvin
            return value - 273.15

    def from_celsius(value, to_scale):
        if to_scale == '1':  # Celsius
            return value
        elif to_scale == '2':  # Fahrenheit
            return value * 9/5 + 32
        elif to_scale == '3':  # Kelvin
            return value + 273.15

    # Convert input to Celsius, then to target scale
    temp_celsius = to_celsius(temp, scale_from)
    result = from_celsius(temp_celsius, scale_to)

    print(f"\n{temp} {scale_dict[scale_from]} is equal to {result:.2f} {scale_dict[scale_to]}.")

    # Weather condition based on Celsius
    print("\nWeather Condition Advice:")
    if temp_celsius < 0:
        print("It's freezing! Dress warmly and beware of ice.")
    elif 0 <= temp_celsius < 10:
        print("Very cold weather. Wear a coat or jacket.")
    elif 10 <= temp_celsius < 20:
        print("Cool weather. A light jacket is recommended.")
    elif 20 <= temp_celsius < 30:
        print("Comfortable temperature. Enjoy your day!")
    elif 30 <= temp_celsius < 40:
        print("It's hot. Stay hydrated and avoid direct sunlight.")
    else:
        print("Extreme heat! Take precautions against heatstroke.")

# Example usage:
improved_temperature_converter()
