def reverse_string(s):
    """
    Reverses the given string.

    Args:
        s (str): The string to reverse.

    Returns:
        str: The reversed string.
    """
    return s[::-1]

if __name__ == "__main__":
    input_str = "hello"
    print("Original:", input_str)
    print("Reversed:", reverse_string(input_str))