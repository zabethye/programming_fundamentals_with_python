text = input()
vowels = "aouei"
text_wo_vowels = list([ch for ch in text if ch.lower() not in vowels])
print("".join(text_wo_vowels))