version = list(map(int, input().split(".")))
version[-1] += 1
for index in range(len(version) -1, -1, -1):
    if version[index] > 9:
        version[index] = 0
        version[index - 1] += 1
print(".".join(str(number) for number in version))