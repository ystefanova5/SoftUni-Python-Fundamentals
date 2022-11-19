import re

total_income = 0
line = input()
while line != "end of shift":
    pattern = r"(%[A-Z]{1}[a-z]+\%)([^\|\$\%\.])*(<[\w]+>)([^\|\$\%\.])*(\|\d+\|)([^\|\$\%\.])*(\d+(\.\d+)*\$)"
    validation = re.findall(pattern, line)
    if validation:
        name_pattern = r"%([A-Z]{1}[a-z]+)\%"
        product_pattern = r"<([\w]+)>"
        count_pattern = r"\|(\d+)\|"
        price_pattern = r"(\d+(\.\d+)*)\$"
        name = re.findall(name_pattern, line)[0]
        product = re.findall(product_pattern, line)[0]
        count = int(re.findall(count_pattern, line)[0])
        price = float(re.findall(price_pattern, line)[0][0])
        cost = count * price
        print(f"{name}: {product} - {cost:.2f}")
        total_income += cost
    line = input()
print(f"Total income: {total_income:.2f}")


################################################   Task Description   ################################################
# 2. SoftUni Bar Income
# Let`s take a break and visit the game bar at SoftUni.
# It is about time for the people behind the bar to go home and you are the person who has to draw the line
# and calculate the money from the products that were sold throughout the day.
# Until you receive a line with text "end of shift" you will be given lines of input.
# But before processing that line you should do some validations first.
# Each valid order should have a customer, product, count and a price:
# • Valid customer's name should be surrounded by '%' and must start with a capital letter,
#   followed by lower-case letters
# • Valid product contains any word character (not only letters) and must be surrounded by '<' and '>'
# • Valid count is an integer, surrounded by '|'
# • Valid price is any real number followed by '$'
# The parts of a valid order should appear in the order given: customer, product, count and a price.
# Between each part there can be other symbols, except ('|', '$', '%' and '.')
# For each valid line print on the console: "{customerName}: {product} - {totalPrice}"
# When you receive "end of shift" print the total amount of money for the day
# rounded to 2 decimal places in the following format: "Total income: {income}".
# Input / Constraints
# • Strings that you have to process until you receive text "end of shift".
# Output
# • Print all of the valid lines in the format "{customerName}: {product} - {totalPrice}"
# • After receiving "end of shift" print the total amount of money for the day
#   rounded to 2 decimal places in the following format: "Total income: {income}"
# • Allowed working time / memory: 100ms / 16MB.
