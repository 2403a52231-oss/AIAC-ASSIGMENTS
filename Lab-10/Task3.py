"""
def c(x,y):
    return x*y/100
a=200
b=15
print(c(a,b))
"""
# Calculate the percentage increase from an old value to a new value

def calculate_percentage_increase(old_value: float, new_value: float) -> float:
    """
    Calculate the percentage increase from old_value to new_value.

    Args:
        old_value (float): The original value.
        new_value (float): The new value.

    Returns:
        float: The percentage increase from old_value to new_value.

    Example:
        >>> calculate_percentage_increase(200, 15)
        20.0
    """
    if old_value == 0:
        return float('inf')  # Avoid division by zero
    increase = new_value - old_value
    percentage_increase = (increase / old_value) * 100
    return percentage_increase

# Example usage:
old_price = 200
new_price = 15
print(f"Percentage increase from {old_price} to {new_price} is {calculate_percentage_increase(old_price, new_price)}%")


