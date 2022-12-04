import re

given_string = input()
pattern = r"\b_([a-zA-Z0-9]+)\b"
matched_words = re.findall(pattern, given_string)
print(",".join(matched_words))

