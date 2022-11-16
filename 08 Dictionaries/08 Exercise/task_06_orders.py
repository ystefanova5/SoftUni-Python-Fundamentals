prices = {}
quantities = {}
command = input().split()
while "buy" not in command:
    current_product = command[0]
    current_price = float(command[1])
    current_quantity = int(command[2])
    prices[current_product] = current_price
    if current_product not in quantities:
        quantities[current_product] = 0
    quantities[current_product] += current_quantity
    command = input().split()
for product in prices:
    total_price = prices[product] * quantities[product]
    print(f"{product} -> {total_price:.2f}")


################################################   Task Description   ################################################
# 6. Orders
# Write a program that keeps the information about products and their prices.
# Each product has a name, a price, and a quantity:
# • If the product doesn't exist yet, add it with its starting quantity.
# • If you receive a product, which already exists,
# increases its quantity by the input quantity and if its price is different, replace the price as well.
# You will receive products' names, prices, and quantities on new lines.
# Until you receive the command "buy", keep adding items.
# Finally, print all items with their names and the total price of each product.
# Input
# • Until you receive "buy", the products will be coming in the format: "{name} {price} {quantity}".
# • The product data is always delimited by a single space.
# Output
# • Print information about each product in the following format:
# "{product_name} -> {total_price}"
# • Format the total price to the 2nd digit after the decimal separator.
