def characters_filter(character_one, character_two):
    filtered_chars = []
    for char in range(ord(character_one) + 1, ord(character_two)):
        filtered_chars.append(chr(char))
    return " ".join(filtered_chars)


char_one = input()
char_two = input()
print(characters_filter(char_one, char_two))
