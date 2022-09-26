number_of_lines = int(input())
tank_capacity = 255
litres_in_tank = 0
for litres in range(number_of_lines):
    litres_to_pour = int(input())
    if tank_capacity - litres_to_pour < 0:
        print("Insufficient capacity!")
    else:
        tank_capacity -= litres_to_pour
        litres_in_tank += litres_to_pour
print(litres_in_tank)