def main():
    # Input: Prompt and validate user input
    while True:
        try:
            # Get integer input
            limit_input = input("Enter a celsius degree: ")
            limit = int(limit_input)
            
            # Validate against absolute zero (-273.15 is absolute zero, so integers below -273 are impossible for Celsius)
            if limit < -273:
                print("Error: Temperature cannot be below absolute zero (-273°C). Please try again.")
                continue
            else:
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Output Header
    # Using formatted string literals to align columns (approx 20 spaces for first column)
    print(f"{'Celsius':<20}{'Fahrenheit'}")
    print("-" * 40) # Prints a dashed line

    # Process: Loop from 0 to the user input
    for celsius in range(limit + 1):
        # Conversion formula: F = (C * 9/5) + 32
        fahrenheit = (celsius * 9/5) + 32
        
        # Output rows
        # The '<20' ensures the celsius value is left-aligned with padding to match the header
        print(f"{celsius:<20}{fahrenheit}")

if __name__ == "__main__":
    main()