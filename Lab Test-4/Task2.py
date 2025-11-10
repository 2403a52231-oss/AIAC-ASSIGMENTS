# /c:/Users/DEEKSHA/Desktop/AIAC/Lab Test-4/Task2.py

student = {"name": "John", "age": 20, "grade": "A"}

# Adding new key-value pair
student["subject"] = "Mathematics"

# Updating existing value
student["age"] = 21

# Deleting a key-value pair
del student["grade"]

# Printing the object
print("Updated student info:", student)
print("Keys:", list(student.keys()))