number_of_users = int(input())
registered_cars = {}
register_user = "register"
unregister_user = "unregister"

for current_user in range(number_of_users):
    command = input().split()

    if command[0] == register_user:
        username = command[1]
        license_plate_number = command[2]
        if username not in registered_cars:
            registered_cars[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate_number}")
    elif command[0] == unregister_user:
        username = command[1]
        if username not in registered_cars:
            print(f"ERROR: user {username} not found")
        else:
            registered_cars.pop(username)
            print(f"{username} unregistered successfully")

for username, number in registered_cars.items():
    print(f"{username} => {number}")
