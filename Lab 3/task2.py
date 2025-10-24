def sort_user_values():
    """
    Prompts the user to enter a list of values separated by spaces,
    sorts them, and prints the sorted list.
    """
    user_input = input("Enter values separated by spaces: ")
    # Try to convert to numbers if possible, otherwise sort as strings
    values = user_input.split()
    try:
        # Try to convert all to float (to handle both int and float)
        numeric_values = [int(v) for v in values]
        sorted_values = sorted(numeric_values)
    except ValueError:
        # If conversion fails, sort as strings
        sorted_values = sorted(values)
    print("Sorted values:", sorted_values)

# Example usage:
sort_user_values()
