orders_counter = int(input())
total_price = 0
for current_order in range(orders_counter):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if not 0.01 <= price_per_capsule <= 100:
        continue
    elif not 1 <= days <= 31:
        continue
    elif not 1 <= capsules_per_day <= 2000:
        continue
    price_per_order = (capsules_per_day * price_per_capsule) * days
    total_price += price_per_order
    print(f"The price for the coffee is: ${price_per_order:.2f}")

print(f"Total: ${total_price:.2f}")
