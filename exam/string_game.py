string = input()

while True:
    current_command = input()

    if current_command == "Done":
        break
    current_command = current_command.split()
    command = current_command[0]

    if command == "Change":
        char = current_command[1]
        replacement = current_command[2]
        string = string.replace(char, replacement)
        print(string)
    elif command == "Includes":
        substring = current_command[1]
        if substring in string:
            print(True)
        else:
            print(False)

    elif command == "End":
        substring = current_command[1]
        lenght_substring = len(string) - len(substring)
        if string[lenght_substring:] == substring:
            print(True)
        else:
            print(False)

    elif command == "Uppercase":
        string = string.upper()
        print(string)

    elif command == "FindIndex":
        char = current_command[1]
        index = string.find(char)
        print(index)

    elif command == "Cut":
        start_index = int(current_command[1])
        count = int(current_command[2])
        string = string[start_index:start_index + count]
        print(string)

