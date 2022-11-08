phonebook = {}
person_phone = input()

while True:
    if person_phone in "0123456789":
        break
    person_phone = person_phone.split("-")
    name = person_phone[0]
    number = person_phone[1]
    if name not in phonebook.keys():
        phonebook[name] = ""
    phonebook[name] = number
    person_phone = input()

for search in range(int(person_phone)):
    searched_name = input()
    if searched_name in phonebook.keys():
        print(f"{searched_name} -> {phonebook[searched_name]}")
        continue
    print(f"Contact {searched_name} does not exist.")
