# 1 - Number Definer
number = float(input())

if number == 0:
    print('zero')

elif number > 0:
    if number < 1:
        print('small positive')
    elif number > 1000000:
        print('large positive')
    else:
        print('positive')

else:
    if abs(number) < 1:
        print('small negative')
    elif abs(number) > 1000000:
        print('large negative')
    else:
        print('negative')

# 2	- Largest of Three Numbers
first_number, second_number, third_number = int(input()), int(input()), int(input())
print(max(first_number, second_number, third_number))

# 3 - Word Reverse
word = input()
print(word[::-1])

# 4 - Even_numbers
number_of_lines = int(input())

for _ in range(number_of_lines):
    current_number = int(input())
    if current_number % 2 != 0:
        print(f'{current_number} is odd!')
        break

else:
    print('All numbers are even.')

# 5 - Number Between 1 and 100
while True:
    number = float(input())
    if 1 <= number <= 100:
        print(f'The number {number} is between 1 and 100')
        break

# 7 - Patterns
number = int(input())

for i in range(1, number + 1):
    print(i * '*')

for j in range(number - 1, 0, -1):
    print(j * '*')