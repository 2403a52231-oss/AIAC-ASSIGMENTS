# Simple user authentication system with register and login functions

users_db = {}

def register_user():
    """
    Registers a new user by asking for a username and password.
    If the username already exists, prompts the user to try again.
    """
    username = input("Enter a new username: ")
    if username in users_db:
        print("Username already exists. Please try a different username.")
        return
    password = input("Enter a new password: ")
    users_db[username] = password
    print("Registration successful!")

def login_user():
    """
    Logs in a user by checking the username and password.
    """
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in users_db and users_db[username] == password:
        print("Login successful!")
    else:
        print("Invalid username or password.")

# Example usage:
register_user()
login_user()
