#prompt the user for a temperature in Fahrenheit
fahrenheit = float(input("Enter temperature in Fahrenheit:"))

# perform the conversion to celsius
celsius = (fahrenheit - 32) * 5 / 9
# This formula is used since Celsius = (Fahrenheit − 32) × 5/9

# generate the output using f-string to format the result
print(f"{fahrenheit}°F is equal to {celsius:2f}°C")
# :.2f in the f-string rounds the Celsius value to 2 decimal places, which is a common convention for temperature reporting. 