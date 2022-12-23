def calculate_price(product, quantity):
    product_price = 0
    if product == "coffee":
        product_price = 1.50
    elif product == "water":
        product_price = 1.00
    elif product == "coke":
        product_price = 1.40
    elif product == "snacks":
        product_price = 2.00
    return f"{(product_price * quantity):.2f}"


input_product = input()
input_quantity = int(input())
print(calculate_price(input_product, input_quantity))


################################################   Task Description   ################################################
# 5. Orders
# Write a function that calculates the total price of an order and returns it. 
# The function should receive one of the following products: 
# "coffee", "coke", "water", or "snacks", and a quantity of the product. 
# The prices for a single piece of each product are: 
#     • coffee - 1.50
#     • water - 1.00
#     • coke - 1.40
#     • snacks - 2.00
# Print the result formatted to the second decimal place.
