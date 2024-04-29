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

# The following function calculates the total marks, average, no of student failed. It use the students_data list
# to calculate the required information
def show_stats(students_data):
    if not students_data:
        print("No data to show statistics.")
        return
    
    total_marks = [student[4] for student in students_data] # Fifth (index 4) being the total marks in students_data list
    avg_mark = sum(total_marks) / len(students_data) # Calculating the average mark
    highest_mark = max(total_marks) # Get highest marks using max() function
    lowest_mark = min(total_marks) # Get lowest marks using min() function
    num_failed = sum(1 for mark in total_marks if mark < 50) # Iterating and summing up 1 for each such occurrence.
    # Identifies high achievers by listing the first element, assuming it's the ID, of each student's data) of students whose marks are 80 or above.
    high_achievers = [student[0] for student in students_data if student[4] >= 80] 

    print("\n|---------------------------------------------------------------|")
    print(f"|Average Mark                             |   {avg_mark:.2f}     ")
    print("|---------------------------------------------------------------|")
    print(f"|Highest Mark:                            |   {highest_mark}      ")
    print("|---------------------------------------------------------------|")
    print(f"|Lowest Mark:                             |   {lowest_mark}      ")
    print("|---------------------------------------------------------------|")
    print(f"|Total Number of Students Failed:         |   {num_failed}      ")
    print("|---------------------------------------------------------------|")
    print(f"|IDs of High Achievers (Total Mark >= 80) |   {high_achievers}   ")
    print("|---------------------------------------------------------------|")


students_data = []

while True:
    student_id = int(input("\nStudent ID:"))
    if student_id <= 0:
        break  # Exit the loop if the ID is non-positive
    
    q1_mark = validate_mark("Enter Q1    : ") 
    q2_mark = validate_mark("Enter Q2    : ") 
    final_mark = validate_mark("Enter Final : ")  
    
    # Calculate the total and round to the nearest whole number
    total = round(q1_mark * 0.20 + q2_mark * 0.30 + final_mark * 0.50)
    
    letter_grade = calculate_grade(total) 
    
    students_data.append([student_id, q1_mark, q2_mark, final_mark, total, letter_grade])

print(students_data)      # Printing the list 
show_stats(students_data) # Printing the stats


