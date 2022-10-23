route = input().split("||")
starting_fuel = int(input())
starting_ammunition = int(input())

for command in route:
    currrent_list = command.split()
    if command == "Titan":
        print("You have reached Titan, all passengers are safe.")
        break
    current_command, current_int = currrent_list[0], int(currrent_list[1])
    if current_command == "Travel":
        if starting_fuel >= current_int:
            starting_fuel -= current_int
            print(f"The spaceship travelled {current_int} light-years.")
        else:
            print("Mission failed.")
            break
    elif current_command == "Enemy":
        if starting_ammunition >= current_int:
            starting_ammunition -= current_int
            print(f"An enemy with {current_int} armour is defeated.")
        elif starting_ammunition < current_int:
            starting_fuel -= current_int * 2
            if starting_fuel >= 0:
                print(f"An enemy with {current_int} armour is outmaneuvered.")
            else:
                print("Mission failed.")
                break
    elif current_command == "Repair":
        ammunitions_added = current_int * 2
        fuel_added = current_int
        starting_ammunition += ammunitions_added
        starting_fuel += fuel_added
        print(f"Ammunitions added: {ammunitions_added}.")
        print(f"Fuel added: {fuel_added}.")

