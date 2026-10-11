# Define absolute zero constants
ABSOLUTE_ZERO_F = -459.67  # Absolute zero in Fahrenheit
ABSOLUTE_ZERO_C = -273.15  # Absolute zero in Celsius

# Prompt the user for the temperature scale
temp_type = input("Enter temperature scale (F for Fahrenheit, C for Celsius): ").strip().upper()

# Prompt the user for the temperature value
temperature = float(input(f"Enter temperature in {temp_type}: "))

# Decision structure based on temperature type
if temp_type == "F":
    # Test the temperature is above absolute zero
    if temperature >= ABSOLUTE_ZERO_F:
        # Convert Fahrenheit to Celsius
        celsius = (temperature - 32) * 5 / 9
        print(f"{temperature}°F is equal to {celsius:.2f}°C")
    else:
        print(f"Invalid temperature: {temperature}°F is below absolute zero ({ABSOLUTE_ZERO_F}°F).")
elif temp_type == "C":
    # Test the temperature is above absolute zero
    if temperature >= ABSOLUTE_ZERO_C:
        # Convert Celsius to Fahrenheit
        fahrenheit = (temperature * 9 / 5) + 32
        print(f"{temperature}°C is equal to {fahrenheit:.2f}°F")
    else:
        print(f"Invalid temperature: {temperature}°C is below absolute zero ({ABSOLUTE_ZERO_C}°C).")
else:
    print(f"Invalid temperature type: '{temp_type}'. Please enter 'F' or 'C'.")