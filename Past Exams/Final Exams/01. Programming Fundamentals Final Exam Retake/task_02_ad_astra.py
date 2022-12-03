import re

text = input()
pattern = r"([#|])([A-Za-z\s]+)\1([0-9]{2}\/[0-9]{2}\/[0-9]{2})\1([0-9]{1,4}|10000)\1"
food_matches = re.findall(pattern, text)
food_list = []
total_calories = 0
for item in food_matches:
    current_food, current_date, current_calories = item[1], item[2], int(item[3])
    total_calories += current_calories
    food_list.append([current_food, current_date, current_calories])
days = total_calories // 2000
print(f"You have food to last you for: {days} days!")
for food in food_list:
    print(f"Item: {food[0]}, Best before: {food[1]}, Nutrition: {food[2]}")


################################################   Task Description   ################################################
# Problem 2 - Ad Astra
# 
# Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
# Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2525#1.
# 
# You are an astronaut who just embarked on a mission across the solar system. 
# Since you will be in space for a long time, you have packed a lot of food with you. 
# Create a program, which helps you identify how much food you have left 
# and gives you information about its expiration date.
# On the first line of the input, you will be given a text string. 
# You must extract the information about the food and calculate the total calories. 
# First, you must extract the food info. It will always follow the same pattern rules:
# • It will be surrounded by "|" or "#" (only one of the two) in the following pattern: 
# #{item name}#{expiration date}#{calories}#   or 
# |{item name}|{expiration date}|{calories}|
# • The item name will contain only lowercase and uppercase letters and whitespace
# • The expiration date will always follow the pattern: "{day}/{month}/{year}", 
#   where the day, month, and year will be exactly two digits long
# • The calories will be an integer between 0-10000
# Calculate the total calories of all food items and then determine how many days you can last with the food you have. 
# Keep in mind that you need 2000kcal a day.
# Input / Constraints
# • You will receive a single string
# Output
# • First, print the number of days you will be able to last with the food you have:
# "You have food to last you for: {days} days!"
# • The output for each food item should look like this:
# "Item: {item name}, Best before: {expiration date}, Nutrition: {calories}"
