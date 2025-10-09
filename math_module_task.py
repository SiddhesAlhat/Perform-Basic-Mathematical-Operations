import math

try:
    number = float(input("Enter a number: "))

    sqrt_value = math.sqrt(number)

    log_value = math.log(number)

    sine_value = math.sin(number)

    print(f"\n Calculations for number: {number}")
    print(f"Square root: {sqrt_value}")
    print(f"Natural logarithm (log base e): {log_value}")
    print(f"Sine (radians): {sine_value}")

except ValueError:
    print("Invalid input! Please enter a valid number greater than 0 for log calculation.")
