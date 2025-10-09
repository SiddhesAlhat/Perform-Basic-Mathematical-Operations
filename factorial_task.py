
def factorial(num):
    if num < 0:
        return "Factorial does not exist for negative numbers"
    elif num == 0 or num == 1:
        return 1
    else:
        result = 1
        for i in range(1, num + 1):
            result *= i
        return result

sample_number = 5
print(f"The factorial of {sample_number} is: {factorial(sample_number)}")
