first_letters_count = int(input())

for first in range(0, first_letters_count):
    for second in range(0, first_letters_count):
        for third in range(0, first_letters_count):
            print(f"{chr(97 + first)}{chr(97 + second)}{chr(97 + third)}")