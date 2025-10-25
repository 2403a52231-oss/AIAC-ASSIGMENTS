def classify_age_group():
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            print("Invalid age.")
        elif age < 13:
            print("You are a Child.")
        elif age < 20:
            print("You are a Teenager.")
        elif age < 60:
            print("You are an Adult.")
        else:
            print("You are a Senior Citizen.")
    except ValueError:
        print("Please enter a valid number.")

# Example usage
classify_age_group()