guests = {}
unliked_meals = 0

while True:
    command = input()
    if command == "Stop":
        break
    command = command.split("-")
    current_command = command[0]
    guest = command[1]
    meal = command[2]

    if current_command == "Like":
        if guest not in guests:
            guests[guest] = []
        if meal not in guests[guest]:
            guests[guest].append(meal)

    elif current_command == "Dislike":
        if guest not in guests:
            print(f"{guest} is not at the party.")
            continue
        elif meal not in guests[guest]:
            print(f"{guest} doesn't have the {meal} in his/her collection.")
        else:
            guests[guest].remove(meal)
            unliked_meals += 1
            print(f"{guest} doesn't like the {meal}.")

for current_guest in guests.keys():
    print(f"{current_guest}: ", end="")
    print(", ". join(guests[current_guest]))

print(f"Unliked meals: {unliked_meals}")
