def get_student_info():
    student = {}
    student['Full name'] = input("Enter full name: ")
    student['Branch'] = input("Enter branch: ")
    student['Sgpa'] = float(input("Enter SGPA: "))
    return student

def main():
    num_students = int(input("How many students? "))
    students = {}
    for i in range(num_students):
        print(f"\nEnter details for student {i+1}:")
        students[f"student_{i+1}"] = get_student_info()
    print("\nNested dictionary of students:")
    print(students)

if __name__ == "__main__":
    main()