import re

pattern = r"\d+"
given_text = input()
while given_text:
    searched_numbers = re.findall(pattern, given_text)
    if searched_numbers:
        print(" ".join(searched_numbers), end=" ")
    given_text = input()
