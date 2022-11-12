command = input()
courses = {}

while command != "end":
    course_name, student_name = command.split(" : ")
    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(student_name)
    command = input()

for current_course in courses:
    registered_students = len(courses[current_course])
    print(f"{current_course}: {registered_students}")
    for student in courses[current_course]:
        print(f"-- {student}")
