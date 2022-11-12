number_of_students = int(input())
students = {}

for current_student in range(number_of_students):
    student_name = input()
    student_grade = float(input())
    if student_name not in students:
        students[student_name] = []
    students[student_name].append(student_grade)

for student in students:
    avg_grade = sum(students[student]) / len(students[student])
    if avg_grade < 4.50:
        continue
    print(f"{student} -> {avg_grade:.2f}")
