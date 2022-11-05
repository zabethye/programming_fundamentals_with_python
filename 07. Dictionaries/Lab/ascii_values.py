list_of_characters = input().split(", ")
dictionary_of_characters = {item: ord(item) for item in list_of_characters}
print(dictionary_of_characters)