# Task description:
# You will be receiving key-value pairs on separate lines separated by ": "
# until you receive the command "statistics". Sometimes you may receive a product more than once.
# In that case, you have to add the new quantity to the existing one.
# When you receive the "statistics" command, print the following:
# "Products in stock:
# - {product1}: {quantity1}
# - {product2}: {quantity2}
# …
# - {productN}: {quantityN}
# Total Products: {count_all_products}
# Total Quantity: {sum_all_quantities}"


bakery_stock = {}
command = input()
while command != "statistics":
    current_key, current_value = command.split(": ")
    if current_key in bakery_stock:
        bakery_stock[current_key] += current_value
    else:
        bakery_stock[current_key] = current_value
    command = input()
products = 0
quantity = 0
print("Products in stock:")
for (key, value) in bakery_stock.items():
    print(f"- {key}: {value}")
    products += 1
    quantity += value
print(f"Total Products: {products}")
print(f"Total Quantity: {quantity}")
