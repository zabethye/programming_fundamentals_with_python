number = int(input())

for x in range(number + 1):
    print(x * "*")
for y in range(number - 1, 0, -1):
    print(y * "*")