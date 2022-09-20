number_strings = int(input())

for string in range(number_strings):
    current_string = input()
    if "," in current_string:
        print(f"{current_string} is not pure!")
    elif "." in current_string:
        print(f"{current_string} is not pure!")
    elif "_" in current_string:
        print(f"{current_string} is not pure!")
    else:
        print(f"{current_string} is pure.")
