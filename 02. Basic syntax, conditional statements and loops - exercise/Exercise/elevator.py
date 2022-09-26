people_counter = int(input())
capacity = int(input())
others = 0
integer_result = people_counter // capacity
if capacity >= people_counter % capacity > 0:
    others += 1
result = integer_result + others
print(result)