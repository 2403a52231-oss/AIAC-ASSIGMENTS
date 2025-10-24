def generate_factorials_up_to_n(n):
    """
    Generate a list of factorials from 0! up to n!.
    Returns a list where the i-th element is i!.
    """
    if n < 0:
        return "Input should be a non-negative integer"
    factorials = [1]
    result = 1
    for i in range(1, n + 1):
        result *= i
        factorials.append(result)
    return factorials

# Example usage:
print(generate_factorials_up_to_n(5))  # Output: [1, 1, 2, 6, 24, 120]
