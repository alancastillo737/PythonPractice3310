import os  # os module to handle PATH flexibility for writing to the file

MIN_PRECIPITATION = 0.0

# Greatest monthly rainfall ever recorded: 366 inches, measured at
# Cherrapunji, Meghalaya, India, in July 1861 (Guinness World Records).
# Used as a generous upper bound since a reasonable "normal" range
# depends heavily on location.
MAX_PRECIPITATION = 366.0

# Name of the text file that stores the month names and precipitation amounts.
OUTPUT_FILE = 'precipitation.txt'


def main():
    # Create a list of the month names, January through December.
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']

    # Use the repetition operator to initialize the precipitation list with 0.0 for each month.
    precipitation = [0.0] * 12

    # Loop through the months and prompt the user for each month's precipitation.
    for i in range(len(months)):
        precipitation[i] = get_precipitation(months[i])

    # analyze the data using list methods and functions
    analyze_precipitation(precipitation, months)

    # Save each month name with its precipitation amount to a text file.
    path = write_precipitation_file(months, precipitation)
    print(f'Data saved to {path}')


"""
Prompt the user to enter precipitation for the given month. Validate the input
until a valid value is received. Use try/except to capture ValueError, which
can result from text-to-float conversion.
"""
def get_precipitation(month):
    while True:
        user_input = input(f'Enter the precipitation for {month}: ')
        try:
            value = float(user_input)
        except ValueError:
            print('Invalid input. Please enter a number.')
            continue

        if value < MIN_PRECIPITATION or value > MAX_PRECIPITATION:
            print(f'Precipitation must be between {MIN_PRECIPITATION} and {MAX_PRECIPITATION}.')
            continue

        return value


"""
Use list functions and methods to calculate annual precipitation total, average
monthly precipitation, the highest precipitation and month, and the lowest
precipitation and month.
"""
def analyze_precipitation(precipitation, months):
    total = sum(precipitation)
    average = total / len(precipitation)
    highest = max(precipitation)
    lowest = min(precipitation)
    highest_index = precipitation.index(highest)
    lowest_index = precipitation.index(lowest)

    print()
    print('Precipitation Analysis')
    print('----------------------')
    print(f'Annual total: {total:.2f}')
    print(f'Average monthly: {average:.2f}')
    print(f'Highest: {months[highest_index]} ({highest:.2f})')
    print(f'Lowest:  {months[lowest_index]} ({lowest:.2f})')
    print()


"""
Write the month and its precipitation to the given file, in the format
January,3.25
Use try/except to capture OSError that can be raised in file writing (return None).
"""
def write_precipitation_file(months, precipitation, filename=OUTPUT_FILE):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
    try:
        with open(path, 'w') as output_file:
            for i in range(len(months)):
                output_file.write(f'{months[i]},{precipitation[i]}\n')
    except OSError as error:
        print(f"Could not save the data to '{path}': {error}")
        return None

    return path


# Call the main function only if this file is run directly.
if __name__ == '__main__':
    main()