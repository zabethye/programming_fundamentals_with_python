strings_counter = int(input())
searched_word = input()
all_strings_list = []
filtered_list = []
for _ in range (strings_counter):
    current_string = input()
    all_strings_list.append(current_string)
for element in all_strings_list:
    if searched_word in element:
        filtered_list.append(element)
print(all_strings_list)
print(filtered_list)