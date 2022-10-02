numbers = input().split()
numbers_to_remove = int(input())
numbers_as_digits = []
final_list = []
for element in numbers:
    numbers_as_digits.append(int(element))
for _ in range(numbers_to_remove):
    numbers_as_digits.remove(min(numbers_as_digits))
for nxt in numbers_as_digits:
    final_list.append(str(nxt))
print(", ".join(final_list))