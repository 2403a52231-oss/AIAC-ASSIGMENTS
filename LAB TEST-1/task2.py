class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def __str__(self):
        return f"Name: {self.name}, Roll No: {self.roll_no}, Marks: {self.marks}"

# Example usage:
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
marks = float(input("Enter marks: "))
student = Student(name, roll_no, marks)
print(student)
