import re

given_text = input()
searched_word = input()
pattern = fr"\b{searched_word}\b"
matched_words = re.findall(pattern, given_text, flags=re.IGNORECASE)
print(len(matched_words))
