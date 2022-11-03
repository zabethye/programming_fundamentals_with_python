product_quantity = input().split()
searched_product = input().split()

bakery_stock = {}

for item in range(len(product_quantity)):
    if item % 2 == 0:
        bakery_stock[product_quantity[item]] = product_quantity[item + 1]

for product in searched_product:
    if product in bakery_stock:
        print(f"We have {bakery_stock[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
