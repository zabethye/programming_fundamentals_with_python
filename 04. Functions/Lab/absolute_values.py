def abs_value(word):
    absolute_list = []
    for element in word:
        num_element = float(element)
        absolute_list.append(abs(num_element))
    return absolute_list


given_word = input().split()
print(abs_value(given_word))
