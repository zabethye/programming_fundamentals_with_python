factor = int(input())
count = int(input())
data_list = []
starting_number = 1
while len(data_list) < count:
    if len(data_list) < count:
        if starting_number % factor == 0:
            data_list.append(starting_number)
    starting_number += 1
print(data_list)
