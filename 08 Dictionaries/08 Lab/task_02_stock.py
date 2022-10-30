products = input().split()
keys = [key for key in products if products.index(key) % 2 == 0]
values = [int(value) for value in products if products.index(value) % 2 != 0]
stock = dict(zip(keys, values))
searched_products = input().split()
for product in searched_products:
    if product in stock:
        print(f"We have {stock[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
