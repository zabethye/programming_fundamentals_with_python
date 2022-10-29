class Party:

    def __init__(self):
        self.people = []


party = Party()

while True:
    name = input()
    if name == "End":
        break
    party.people.append(name)

going_people = ", ".join(party.people)
print(f"Going: {going_people}")
print(f"Total: {len(party.people)}")
