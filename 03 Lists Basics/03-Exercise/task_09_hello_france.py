items_collection = input()
budget = int(input())
ticket_price = 150
items_collection_list = items_collection.split("|")
new_prices_list = []
profit = 0
sold_items_value = 0
budget_is_enough = False
for i in range(len(items_collection_list)):
    current_items = items_collection_list[i]
    current_items_list = current_items.split("->")
    current_item_type = current_items_list[0]
    current_item_price = float(current_items_list[-1])
    if current_item_type == "Clothes" and current_item_price <= 50:
        item_price_is_in_range = True
    elif current_item_type == "Shoes" and current_item_price <= 35:
        item_price_is_in_range = True
    elif current_item_type == "Accessories" and current_item_price <= 20.50:
        item_price_is_in_range = True
    else:
        item_price_is_in_range = False
    if item_price_is_in_range and budget >= current_item_price:
        budget -= current_item_price
        current_item_new_price = current_item_price * 1.4
        profit += current_item_new_price - current_item_price
        sold_items_value += current_item_new_price
        new_prices_list.append(current_item_new_price)
for j in range(len(new_prices_list)):
    new_price = new_prices_list[j]
    print(f"{new_price:.2f}", end=" ")
print()

print(f"Profit: {profit:.2f}")
if (sold_items_value + budget) >= ticket_price:
    print("Hello, France!")
else:
    print("Not enough money.")


################################################   Task Description   ################################################
# 9. * Hello, France
# You want to go to France by train, and the train ticket costs exactly 150$. 
# You do not have enough money, so you decide to buy some items with your budget 
# and then sell them at a higher price – with a 40% markup.
# You will receive a collection of items and a budget in the following format:
# {type->price|type->price|type->price……|type->price}
# {budget}
# The prices for each of the types cannot exceed a specific price, which is given below:
# Type	        Maximum Price
# Clothes	    50.00
# Shoes	        35.00
# Accessories	20.50
# If a price for a particular item is higher than the maximum price, don't buy it. 
# Every time you buy an item, you have to reduce the budget with its price value. 
# If you don't have enough money for it, you can't buy it. Buy as many items as you can.
# Next, you should increase the price of each item you have successfully bought by 40% and then sell it. 
# Calculate if the budget after selling all the items is enough for buying the train ticket.
# Input / Constraints
#     • On the 1st line, you will receive the items with their prices 
#       in the format described above – real numbers in the range [0.00……1000.00]
#     • On the 2nd line, you are going to be given the budget – a real number in the range [0.0….1000.0]
# Output
#     • First, print the list with the bought item’s new prices, 
#       formatted to the second decimal point in the following format:
#       "{price1} {price2} {price3} … {priceN}"
#     • Second, print the profit, formatted to the second decimal point in the following format:
#       "Profit: {profit}"
#     • Finally:
#         o If the budget is enough for buying the train ticket, print: "Hello, France!" 
#         o Otherwise, print: "Not enough money."
