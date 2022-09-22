number_of_orders = int(input())
total_sum = 0
for order in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    coffee_price = price_per_capsule * capsules_per_day * days
    if 0.01 <= price_per_capsule <= 100 and 1 <= days <= 31 and 1 <= capsules_per_day <= 2000:
        total_sum += coffee_price
        print(f"The price for the coffee is: ${coffee_price:.2f}")
print(f"Total: ${total_sum:.2f}")
