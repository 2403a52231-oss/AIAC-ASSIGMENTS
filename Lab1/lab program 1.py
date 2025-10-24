def is_string_palindrome(value):
    if not isinstance(value, str):
        return "Input is not a string."
    cleaned = ''.join(c.lower() for c in value if c.isalnum())
    if cleaned == cleaned[::-1]:
        return "Valid palindrome."
    else:
        return "Not a palindrome."

# Example usage:
user_input = input("Enter a value: ")
result = is_string_palindrome(user_input)
print(result)
