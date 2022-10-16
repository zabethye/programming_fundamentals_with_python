message = input().split()

output = []

for word in message:
    digits = []
    count = 0
    split_message = [ch for ch in word]
    for char in split_message:
        if char.isdigit():
            digits.append(char)
            count += 1
    ascii_char = int("".join(digits))
    character = chr(ascii_char)
    split_message = split_message[count:]
    split_message.insert(0, character)
    split_message[1], split_message[-1] = split_message[-1], split_message[1]
    output.append(split_message)

for current_word in output:
    print("".join(current_word), end=" ")
