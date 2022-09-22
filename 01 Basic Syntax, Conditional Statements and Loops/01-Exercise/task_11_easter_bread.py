budget = float(input())
flour_price = float(input())
eggs_price = flour_price * 0.75
milk_price = flour_price * 1.25
price_per_bread = flour_price + eggs_price + milk_price * 0.25
number_of_breads = 0
colored_eggs = 0
while budget > price_per_bread:
    budget -= price_per_bread
    number_of_breads += 1
    colored_eggs += 3
    if number_of_breads % 3 == 0:
        colored_eggs -= (number_of_breads - 2)
    if budget < price_per_bread:
        break
money_left = budget
print(f"You made {number_of_breads} loaves of Easter bread!"
      f" Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.")
