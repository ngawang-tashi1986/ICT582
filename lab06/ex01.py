# The following program takes in marks for student and calculate the grades, average, highest and lowest mark in a List

# The following function checks the validation of marks. 
# The function uses input(prompt) to display the prompt string in the console and wait for the user to enter marks. 
def validate_mark(prompt):
    while True:
        mark = int(input(prompt)) 
        if 0 <= mark <= 100:
                return mark
        else:
            print("Error!!! Student mark must be between 0 and 100.")

# Following function calculate the grade from given marks
def calculate_grade(total_mark):
    if total_mark >= 80:
        return "HD"  # High Distinction
    elif total_mark >= 70:
        return "D"   # Distinction
    elif total_mark >= 60:
        return "C"   # Credit
    elif total_mark >= 50:
        return "P"   # Pass
    else:
        return "N"   # Fail
    
students_data = {}

while True:

    student_id = int(input("\nStudent ID:"))
    if student_id <= 0:
        break  # Exit the loop if the ID is non-positive
    elif not 1000 <= int(student_id) <= 2000: # Validate the student ID
         print("Invalid Student ID, please enter a number between 1000 and 2000.")
         continue
      
    name = input("Enter student name : ")
    q1_mark = validate_mark("Enter Q1 mark      : ") 
    q2_mark = validate_mark("Enter Q2 mark      : ") 
    final_mark = validate_mark("Enter Final mark   : ")  
    
    # Calculate the total and round to the nearest whole number
    total = round(q1_mark * 0.20 + q2_mark * 0.30 + final_mark * 0.50)
    
    letter_grade = calculate_grade(total) 

    # Store data in a dictionary with student ID as the key
    students_data[student_id] = {
        'Name': name,
        'StudentID': int(student_id),
        'Q1': q1_mark,
        'Q2': q2_mark,
        'Final': final_mark,
        'Total': total,
        'Grade': letter_grade
    }

   
for student in students_data.values():
        print(f"Name       : {student['Name']}")
        print(f"StudentID  : {student['StudentID']}")
        print(f"Q1 Mark    : {student['Q1']}")
        print(f"Q2 Mark    : {student['Q2']}")
        print(f"Final Mark : {student['Final']}")
        print(f"Ttoal Mark : {student['Total']}")
        print(f"Grade      : {student['Grade']}\n")


