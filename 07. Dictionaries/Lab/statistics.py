command = input()
products_in_stock = {}
while command != "statistics":
    product, quantity = command.split(": ")
    if product not in products_in_stock.keys():
        products_in_stock[product] = 0
    products_in_stock[product] += int(quantity)
    command = input()
print("Products in stock:")
for item, qty in products_in_stock.items():
    print(f"- {item}: {qty}")
print(f"Total Products: {len(products_in_stock.keys())}\nTotal Quantity: {sum(products_in_stock.values())}")