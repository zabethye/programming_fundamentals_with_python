resource = input()
resources = {}

while resource != "stop":
    quantity = int(input())
    if resource not in resources.keys():
        resources[resource] = 0
    resources[resource] += quantity
    resource = input()
[print(f"{item} -> {pieces}") for item, pieces in resources.items()]
#
# for item, pieces in resources.items():
#     print(f"{item} -> {pieces}")