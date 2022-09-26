num_of_chars = int(input())
result = 0
for char in range(num_of_chars):
    current_char = input()
    char_points = ord(current_char)
    result += char_points
print(f"The sum equals: {result}")
