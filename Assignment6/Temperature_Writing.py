from pathlib import Path

MIN_CELSIUS = 0
MAX_CELSIUS = 50

SCRIPT_DIR = Path(__file__).resolve().parent
FORLOOP_FILE = SCRIPT_DIR / "temperature_forloop.txt"
WHILELOOP_FILE = SCRIPT_DIR / "temperature_whileloop.txt"


def main():
    celsius = get_celsius()
    write_temperature_file_forloop(celsius)
    write_temperature_file_whileloop(celsius)


def get_celsius():
    """Prompt until a valid integer Celsius value in [0, 50] is entered."""
    good_value_received = False
    while not good_value_received:
        celsius_text = input(
            f"Enter a celsius degree ({MIN_CELSIUS}-{MAX_CELSIUS}): "
        )
        try:
            celsius = int(celsius_text)
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue
        if celsius < MIN_CELSIUS or celsius > MAX_CELSIUS:
            print(
                f"Invalid input. Please enter a temperature between "
                f"{MIN_CELSIUS} and {MAX_CELSIUS}."
            )
        else:
            good_value_received = True
    return celsius


def write_temperature_file_forloop(celsius):
    """Write the Celsius -> Fahrenheit table using a for-loop."""
    with open(FORLOOP_FILE, "w") as outfile:
        outfile.write(f'{"Celsius":>8}\t\t{"Fahrenheit":>8}\n')
        outfile.write("------------------------------------\n")
        for degree in range(celsius + 1):
            fahrenheit = (degree * 1.8) + 32
            outfile.write(f"{degree:>8}\t\t{fahrenheit:>8.2f}\n")


def write_temperature_file_whileloop(celsius):
    with open(WHILELOOP_FILE, "w") as outfile:
        outfile.write(f'{"Celsius":>8}\t\t{"Fahrenheit":>8}\n')
        outfile.write("------------------------------------\n")
        degree = 0
        while degree <= celsius:
            fahrenheit = (degree * 1.8) + 32
            outfile.write(f"{degree:>8}\t\t{fahrenheit:>8.2f}\n")
            degree += 1


if __name__ == "__main__":
    main()