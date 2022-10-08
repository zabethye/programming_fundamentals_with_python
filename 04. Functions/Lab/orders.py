current_product = input()
needed_quantity = int(input())


def calculating_price(product, quantity):
    price = 0
    if product == "coffee":
        price = 1.5
    elif product == "water":
        price = 1
    elif product == "coke":
        price = 1.4
    elif product == "snacks":
        price = 2
    price_for_product = price * quantity
    return f"{price_for_product:.2f}"


print(calculating_price(current_product, needed_quantity))
