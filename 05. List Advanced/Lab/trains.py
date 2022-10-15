number_of_wagons = int(input())
train = [0] * number_of_wagons
while True:
  command = input().split()
  current_command = command[0]
  if current_command == "End":
    break
  if current_command == "add":
    people_to_add = int(command[1])
    train[-1] += people_to_add
  elif current_command == "insert":
    index = int(command[1])
    persons_to_add = int(command[2])
    train[index] += persons_to_add
  elif current_command == "leave":
    index = int(command[1])
    persons_to_leave = int(command[2])
    train[index] -= persons_to_leave
print(train)