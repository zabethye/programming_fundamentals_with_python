sentence = input()


def round_sentence(words):
    words_list = words.split()
    new_list = []
    for number in words_list:
        current_word = float(number)
        new_list.append(round(current_word))
    return new_list


print(round_sentence(sentence))
