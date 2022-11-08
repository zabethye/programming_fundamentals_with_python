orders = {}
command = input()

while command != "buy":
    product, price, qty = command.split()
    if product not in orders.keys():
        orders[product] = [float(price), int(qty)]
    else:
        orders[product][0] = float(price)
        orders[product][1] += int(qty)
    command = input()

for current_order in orders:
    total_price = orders[current_order][0] * orders[current_order][1]
    print(f"{current_order} -> {total_price:.2f}")
