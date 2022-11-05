command = input().split(":")
courses = {}
while len(command) > 1:
    name, id, course = command[0], command[1], command[2]
    if course not in courses.keys():
        courses[course] = []
    courses[course].append(f"{name} - {id}")
    command = input().split(":")
searched_course = command[0].replace("_", " ")
[print(item) for item in courses[searched_course]]
