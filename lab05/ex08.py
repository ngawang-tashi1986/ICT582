import shutil

def add_student(students):
    student = {}
    student['ID'] = input("Enter student ID: ")
    student['Name'] = input("Enter student name: ")
    student['GPA'] = float(input("Enter student GPA (0~4): "))
    while student['GPA'] < 0 or student['GPA'] > 4:
        print("Invalid GPA. GPA should be between 0 and 4.")
        student['GPA'] = float(input("Enter student GPA (0~4): "))
    student['Major'] = input("Enter student major: ")
    student['Contact'] = input("Enter contact number: ")
    students.append(student)
    print("Student added successfully.")

def search_student(students):
    id = input("Enter student ID to search: ")
    for student in students:
        if student['ID'] == id:
            print("Student found: ", student)
            return
    print("Student not found.")

def delete_student(students):
    id = input("Enter student ID to delete: ")
    for i, student in enumerate(students):
        if student['ID'] == id:
            del students[i]
            print("Student deleted successfully.")
            return
    print("Student not found.")

def display_deans_list(students):
    print("Dean's List Students:")
    for student in students:
        if student['GPA'] >= 3.75:
            print(student)

def display_all_students(students):
    print("All Students Details:")
    for student in students:
        print(student)

students = []
while True:
    columns = shutil.get_terminal_size().columns
    print("|------------------------------------------------|".center(columns))
    print("|            STUDENT MANAGEMENT SYSTEM           |".center(columns))
    print("|------------------------------------------------|".center(columns))
    print("|                1. Add Student                  |".center(columns))
    print("|------------------------------------------------|".center(columns))
    print("|               2. Search Student                |".center(columns))
    print("|------------------------------------------------|".center(columns))
    print("|               3. Delete Student                |".center(columns))
    print("|------------------------------------------------|".center(columns))
    print("|          4. Display Dean's List Students       |".center(columns))
    print("|------------------------------------------------|".center(columns))
    print("|             5. Display All Students            |".center(columns))
    print("|------------------------------------------------|".center(columns))
    print("|                  6. Exit                       |".center(columns))
    print("|------------------------------------------------|".center(columns))
    choice = input("\nEnter your choice: ")
    
    if choice == '1':
        add_student(students)
    elif choice == '2':
        search_student(students)
    elif choice == '3':
        delete_student(students)
    elif choice == '4':
        display_deans_list(students)
    elif choice == '5':
        display_all_students(students)
    elif choice == '6':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")

