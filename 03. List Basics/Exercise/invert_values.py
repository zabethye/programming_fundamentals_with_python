given_string = input().split()
opposite_list = []
for element in given_string:
    opposite_element = -int(element)
    opposite_list.append(opposite_element)
print(opposite_list)
