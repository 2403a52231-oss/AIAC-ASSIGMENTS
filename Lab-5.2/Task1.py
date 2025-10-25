import hashlib
import getpass

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register(users):
    username = input("Enter a new username: ").strip()
    if username in users:
        print("Username already exists. Please try another.")
        return
    password = getpass.getpass("Enter a new password: ")
    confirm = getpass.getpass("Confirm password: ")
    if password != confirm:
        print("Passwords do not match.")
        return
    users[username] = hash_password(password)
    print("Registration successful.")

def login(users):
    username = input("Enter your username: ").strip()
    if username not in users:
        print("Username not found.")
        return
    password = getpass.getpass("Enter your password: ")
    if users[username] == hash_password(password):
        print("Login successful. Welcome,", username)
    else:
        print("Incorrect password.")

def main():
    users = {}
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Select an option: ").strip()
        if choice == '1':
            register(users)
        elif choice == '2':
            login(users)
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()


