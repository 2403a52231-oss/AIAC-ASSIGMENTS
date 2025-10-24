def generate_factorial(n):
    """
    Generate the factorial of a non-negative integer n.
    Returns the factorial value, or an error message for negative input.
    """
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

try:
    user_input = int(input("Enter a number to calculate factorial: "))
    result = generate_factorial(user_input)
    print(f"The factorial of {user_input} is: {result}")
except ValueError:
    print("Please enter a valid integer!")

