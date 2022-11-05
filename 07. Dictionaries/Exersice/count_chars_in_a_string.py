word = input()
occurrences = {}

for char in word:
    if char == " ":
        continue
    if char not in occurrences:
        occurrences[char] = 0
    occurrences[char] += 1

[print(f"{chars} -> {times}") for chars, times in occurrences.items()]