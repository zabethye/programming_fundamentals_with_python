words = input().split()
dict_words = {}
for word in words:
    if word.lower() not in dict_words.keys():
        dict_words[word.lower()] = 0
    dict_words[word.lower()] += 1
for item in dict_words.keys():
    if dict_words[item] % 2 != 0:
        print(item, end=" ")
