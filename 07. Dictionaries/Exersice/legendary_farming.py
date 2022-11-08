materials = {"shards": 0, "fragments": 0, "motes": 0}
given_materials = input().split()
is_obtained = False

while not is_obtained:
    for item in range(len(given_materials)):
        if item % 2 != 0:
            if given_materials[item].lower() not in materials.keys():
                materials[given_materials[item].lower()] = 0
            materials[given_materials[item].lower()] += int(given_materials[item - 1])
        if materials["shards"] >= 250:
            print("Shadowmourne obtained!")
            materials["shards"] -= 250
            is_obtained = True
        elif materials["fragments"] >= 250:
            print("Valanyr obtained!")
            materials["fragments"] -= 250
            is_obtained = True
        elif materials["motes"] >= 250:
            print("Dragonwrath obtained!")
            materials["motes"] -= 250
            is_obtained = True
        if is_obtained:
            break
    if is_obtained:
        break
    given_materials = input().split()

for item, quantity in materials.items():
    print(f"{item}: {quantity}")