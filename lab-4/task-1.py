def is_valid_indian_mobile(number):
    """
    Validates if the given number is a valid Indian mobile number.
    Must start with 6, 7, 8, or 9 and be exactly 10 digits.
    """
    return number.isdigit() and len(number) == 10 and number[0] in '6789'

# Example usage:
user_input = input("Enter your mobile number: ")
if is_valid_indian_mobile(user_input):
    print("Valid Indian mobile number.")
else:
    print("Invalid mobile number.")