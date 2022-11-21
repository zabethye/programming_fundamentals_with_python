given_string = input()
new_string = ""
strength = 0

for index in range(len(given_string)):
    if strength > 0 and given_string[index] != ">":
        strength -= 1
    elif given_string[index] == ">":
        new_string += given_string[index]
        strength += int(given_string[index + 1])
    else:
        new_string += given_string[index]

print(new_string)
