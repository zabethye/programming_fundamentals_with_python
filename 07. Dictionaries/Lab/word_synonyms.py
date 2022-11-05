word_count = int(input())
synonyms_dict = {}
for word in range(word_count):
    current_word = input()
    current_synonym = input()
    if current_word not in synonyms_dict.keys():
        synonyms_dict[current_word] = []
    synonyms_dict[current_word].append(current_synonym)
    
for item in synonyms_dict.keys():
    print(f"{item} - ", end="")
    for synonym in synonyms_dict[item]:
        if synonym == synonyms_dict[item][-1]:
            print(f"{synonym}")
            break
        print(f"{synonym}", end=", ")

