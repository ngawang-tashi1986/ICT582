def validate_mark(mark):
    while True:
        if mark >=0 and mark<=100 and mark.is_integer():
            f_mark = int(mark)
            break
        else:
            mark = float(input("ENter the new mark"))
    return f_mark

def calculateTotal(q1, q2, f):
    total = q1 * 0.20 + q2 * 0.30 + f * 0.50
    return total

def final_grade(total):
    grade = ''

    if total >= 80:
        grade = 'HD'
    elif total >= 70:
        grade = 'D'
    elif total >= 60:
        grade = 'C'
    elif total >= 50:
        grade = 'P'
    else:
        grade = 'N'
    return grade

all_student = []
while True:
    student = []
    st_id = input("Enter a student id : ")

    if int(st_id) <= 0:
        break
    else:
        student.append(st_id)

        q1 = float(input("Enter quiz 1 mark (0-100) : "))
        q1_mark  = validate_mark(q1)
        student.append(q1_mark)

        q2 = float(input("Enter quiz 2 mark (0-100) : "))
        q2_mark  = validate_mark(q2)
        student.append(q2_mark)

        f = float(input("Enter final mark (0-100) : "))
        f_mark  = validate_mark(f)
        student.append(f_mark)
        #print(q1_mark)

        total = calculateTotal(q1_mark, q2_mark, f_mark)

        student.append(total)

        grade = final_grade(total)
        student.append(grade)
        all_student.append(student)

print(all_student)


