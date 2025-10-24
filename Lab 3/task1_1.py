def generate_factorial(n):
    """
    Generate the factorial of a non-negative integer n.
    Factorial of n (n!) is the product of all positive integers less than or equal to n.
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

# Example usage:
print(generate_factorial(5))  # Output: 120
print(generate_factorial(0))  # Output: 1
print(generate_factorial(10)) # Output: 3628800
print(generate_factorial(-1)) # Output: Factorial is not defined for negative numbers


