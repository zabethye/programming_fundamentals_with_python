word = input()
count_times = int(input())


def repeat_string(given_string, counter):
    new_string = ""
    for strng in range(counter):
        new_string += given_string
    return new_string


print(repeat_string(word, count_times))
