total_price = 0
price_without_taxes = 0
taxes = 0
get_discount = False
while True:
    command = input()
    if command == "special":
        get_discount = True
        break
    if command == "regular":
        break
    current_price = float(command)
    if current_price < 0:
        print("Invalid price!")
    else:
        taxes += current_price * 0.2
        total_price += current_price * 1.2
price_without_taxes = total_price - taxes
if get_discount:
    total_price *= 0.90
if total_price == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {price_without_taxes:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_price:.2f}$")
