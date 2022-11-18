import re

purchase_info = input()
purchases = {}
total_cost = 0
print("Bought furniture:")
while purchase_info != "Purchase":
    pattern = r">>(?P<furniture_name>[A-Za-z]+)<<(?P<price>\d+(\.\d+)?)!(?P<quantity>\d+)\b"
    current_purchase = re.finditer(pattern, purchase_info)
    if current_purchase:
        for product in current_purchase:
            info = product.groupdict()
            product_name = info["furniture_name"]
            price = float(info["price"])
            quantity = int(info["quantity"])
            total_cost += price * quantity
            print(product_name)
    purchase_info = input()
print(f"Total money spend: {total_cost:.2f}")


################################################   Task Description   ################################################
# 5. Furniture
# Write a program that calculates the total cost of bought furniture.
# You will be given information about each purchase on separate lines until you receive the command "Purchase".
# Valid information should be in the format: ">>{furniture_name}<<{price}!{quantity}".
# The price could be a floating-point or integer number.
# You should store the names of the furniture and the total price.
# In the end, print the name of each bought furniture and the total cost, formatted to the second decimal point:
# "Bought furniture:
# {1st name}
# {2nd name}
# …
# {N name}
# Total money spend: {total_cost}"
