def check_null_values(dragon_damage, dragon_health, dragon_armor):
    if dragon_damage == "null":
        dragon_damage = 45
    if dragon_health == "null":
        dragon_health = 250
    if dragon_armor == "null":
        dragon_armor = 10
    return dragon_damage, dragon_health, dragon_armor


dragons = {}
number_of_entries = int(input())
for entry in range(number_of_entries):
    type, name, damage, health, armor = input().split()
    damage, health, armor = check_null_values(damage, health, armor)
    if type not in dragons:
        dragons[type] = {"total damage": 0, "total health": 0, "total armor": 0}
    if name not in dragons[type]:
        dragons[type][name] = {}
    else:
        dragons[type]["total damage"] -= dragons[type][name]["damage"]
        dragons[type]["total health"] -= dragons[type][name]["health"]
        dragons[type]["total armor"] -= dragons[type][name]["armor"]
    dragons[type][name]["damage"] = int(damage)
    dragons[type][name]["health"] = int(health)
    dragons[type][name]["armor"] = int(armor)
    dragons[type]["total damage"] += int(damage)
    dragons[type]["total health"] += int(health)
    dragons[type]["total armor"] += int(armor)

statistic_keys = ["total damage", "total health", "total armor"]

for dragon_type, dragon in dragons.items():
    number_of_dragons = len(dragons[dragon_type]) - 3
    average_damage = dragons[dragon_type]["total damage"] / number_of_dragons
    average_health = dragons[dragon_type]["total health"] / number_of_dragons
    average_armor = dragons[dragon_type]["total armor"] / number_of_dragons
    print(f"{dragon_type}::({average_damage:.2f}/{average_health:.2f}/{average_armor:.2f})")
    sorted_dragons = dict(sorted(dragon.items(), key=lambda x: x[0]))
    for key, value in sorted_dragons.items():
        if key not in statistic_keys:
            print(f"-{key} -> damage: {value['damage']}, health: {value['health']}, armor: {value['armor']}")


###################################### Task Description ######################################
# 5. Dragon Army
# Heroes III is the best game ever. Everyone loves it and everyone plays it all the time. 
# Simon is no exclusion to this rule. 
# His favorite units in the game are all types of dragons – black, red, gold, azure etc. 
# He likes them so much that he gives them names and keeps logs of their stats: damage, health, and armor. 
# The process of aggregating all the data is quite tedious, so he would like to have a program doing it. 
# Since he is no programmer, it's your task to help him.
# You need to categorize dragons by their type. 
# For each dragon, identified by name, keep information about his stats (damage, health, and armor). 
# Type is preserved as in the order of input, but dragons are sorted alphabetically by their name. 
# For each type, you should also print the average damage, health, and armor of the dragons. 
# For each dragon, print his own stats.
# There may be missing stats in the input, though. If a stat is missing you should assign it default values. 
# Default values are as follows: health 250, damage 45, and armor 10. Missing stat will be marked by "null".
# The input is in the following format "{type} {name} {damage} {health} {armor}".
# The "type" and the "name" are strings. The "damage", the "health", and the "armor" are integers. 
# Any of the integers may be assigned "null" value. See the examples below for better understanding of your task.
# If the same dragon is added a second time, the new stats should overwrite the previous ones. 
# Two dragons are considered equal if they match by both name and type.
# Input
# • On the first line, you are given number N -> the number of dragons to follow.
# • On the next N lines, you are given input in the above-described format. 
#   There will be a single space separating each element.
# Output
# • Print the aggregated data on the console.
# • For each type, print average stats of its dragons in format "{type}::({damage}/{health}/{armor})".
# • Damage, health, and armor should be rounded to two digits after the decimal separator.
# • For each dragon, print its stats in format "-{Name} -> damage: {damage}, health: {health}, armor: {armor}".
# Constraints
# • N is in range [1…100].
# • The dragon type and name are one word only, starting with capital letter.
# • Damage health and armor are integers in range [0 … 100000] or null.
