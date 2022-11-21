given_string = input()
new_string = ""
for char in given_string:
    new_char = chr(ord(char) + 3)
    new_string += new_char
print(new_string)
