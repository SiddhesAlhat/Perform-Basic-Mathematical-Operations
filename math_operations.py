
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

if num2 != 0:
    division = num1 / num2
else:
    division = "Error! Division by zero."

# Display results
print("\nResults:")
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
