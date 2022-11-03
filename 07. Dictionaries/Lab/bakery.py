food_quantities = input().split()
bakery = {}
for item in range(len(food_quantities)):
    if item % 2 == 0:
        bakery[food_quantities[item]] = int(food_quantities[item + 1])

print(bakery)