event_name = input()
coffee_needed = 0
events = ["CODING", "DOG", "CAT", "MOVIE"]
while event_name != "END":
    if event_name.upper() in events:
        if event_name.islower():
            coffee_needed += 1
        elif event_name.isupper():
            coffee_needed += 2
    if coffee_needed > 5:
        print("You need extra sleep")
        break
    event_name = input()
if coffee_needed <= 5:
    print(coffee_needed)
