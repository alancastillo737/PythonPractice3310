# TODO: define Global Constants
ABSOLUTE_ZERO_F = -459.67  # Absolute zero in Fahrenheit
ABSOLUTE_ZERO_C = -273.15  # Absolute zero in Celsius


def main():
    temperature_type = get_temperature_type()
    temperature = get_temperature(temperature_type)
    display_conversion(temperature_type, temperature)


# TODO: complete this function which prompt user for the temperature type (C or F) until a valid input is received.
def get_temperature_type():
    while True:
        # Prompt user for input
        user_input = input("Enter the type of temperature (F for Fahrenheit, C for Celsius): ")
        # Clean up input: strip whitespace and make uppercase for comparison
        temp_type = user_input.strip().upper()
        
        # Check if input is valid
        if temp_type == 'F' or temp_type == 'C':
            return temp_type
        else:
            # Error message for invalid type (matches screenshot 3)
            print("Invalid temperature type. Please enter 'F' for Fahrenheit or 'C' for Celsius.")


# TODO: complete this function which prompt user for the temperature until a valid value is received.
def get_temperature(temperature_type):
    # Determine which absolute zero threshold to use based on type
    if temperature_type == 'F':
        limit = ABSOLUTE_ZERO_F
    else:
        limit = ABSOLUTE_ZERO_C
        
    while True:
        try:
            # Prompt for the temperature value
            # Note: Screenshot shows simple prompt "Enter the temperature you want to convert: "
            val_input = input("Enter the temperature you want to convert: ")
            temperature = float(val_input)
            
            # Check if value is physically possible (above absolute zero)
            if temperature >= limit:
                return temperature
            else:
                # Error message for temperature below absolute zero
                # Note: The screenshot shows the limit displayed with 2 decimal places
                print(f"Invalid temperature. Please enter a temperature above absolute zero ({limit:.2f}).")
                
        except ValueError:
            # Handle cases where input is not a number
            print("Invalid input. Please enter a numeric value.")


# TODO: complete this function which perform conversion based on the type
def display_conversion(temperature_type, temperature):
    if temperature_type == 'F':
        # Convert Fahrenheit to Celsius
        celsius = (temperature - 32) * 5 / 9
        # Output format matches the first screenshot: "The temperature in Celsius is: 37.78"
        print(f"The temperature in Celsius is: {celsius:.2f}")
    elif temperature_type == 'C':
        # Convert Celsius to Fahrenheit
        fahrenheit = (temperature * 9 / 5) + 32
        # Output format matches the last screenshot: "The temperature in Fahrenheit is: -148.00"
        print(f"The temperature in Fahrenheit is: {fahrenheit:.2f}")


if __name__ == "__main__":
    main()