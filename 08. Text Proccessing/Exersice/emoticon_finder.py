given_string = input()

for index in range(len(given_string)):
    if given_string[index] == ":" and index != len(given_string) - 1:
        print(f":{given_string[index + 1]}")
