def greet_user(name, gender):
    gender_lower = gender.lower()
    if gender_lower == "male":
        title = "Mr."
    elif gender_lower == "female":
        title = "Ms."
    else:
        title = ""
    if title:
        return f"Hello, {title} {name}! Welcome."
    else:
        return f"Hello, {name}! Welcome."
if __name__ == "__main__":
    name = input("Enter your name: ")
    gender = input("Enter your gender (male/female/other): ")
    print(greet_user(name, gender))
