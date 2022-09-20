budget = int(input())

copy_budget = budget
current_price = input()

while current_price != "End":
    current_price = int(current_price)
    copy_budget -= current_price
    if copy_budget < 0:
        print("You went in overdraft!")
        break
    current_price = input()

if current_price == "End":
    print("You bought everything needed.")
