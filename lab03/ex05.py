# Initialize counters for each grade and total marks
grade_hd = grade_d = grade_c = grade_p = grade_n = total_marks = 0

# Read marks until the user enters "END/end"
while True:
    individual_marks = input("Enter list of marks or 'end/END' to finish: ")
    if individual_marks.upper() == "END":
        break
    else:
        individual_marks = int(individual_marks)  # Convert the mark to an integer for comparison

    # Increment total marks
    total_marks += 1

    # Increment grade counters based on the mark
    if 80 <= individual_marks <= 100:
        grade_hd += 1
    elif 70 <= individual_marks < 80:
        grade_d += 1
    elif 60 <= individual_marks < 70:
        grade_c += 1
    elif 50 <= individual_marks < 60:
        grade_p += 1
    elif 0 <= individual_marks < 50:
        grade_n += 1
    else:
        print("Mark is out of range. Please enter a value between 0 and 100.")
        total_marks -= 1  # Adjust for out-of-range input

# Calculate the percentage of students who fail the unit
if total_marks > 0:
    fail_percentage = (grade_n / total_marks) * 100
else:
    fail_percentage = 0

# Print the results
print(f"Total number of marks           : {total_marks}")
print(f"Number of students receiving HD : {grade_hd}")
print(f"Number of students receiving D  : {grade_d}")
print(f"Number of students receiving C  : {grade_c}")
print(f"Number of students receiving P  : {grade_p}")
print(f"Number of students receiving N  : {grade_n}")
print(f"{fail_percentage:.1f}% of students have failed the unit.")
