import re

count = int(input())
pattern = r"(^\|([A-Z]{4,})\|)\:(#([A-Za-z]+\s[A-Za-z]+)#)"
for validations in range(count):
    current_boss = input()
    valid_match = re.search(pattern, current_boss)
    if valid_match:
        name = valid_match.groups()[1]
        title = valid_match.groups()[3]
        strength = len(name)
        armor = len(title)
        print(f"{name}, The {title}")
        print(f">> Strength: {strength}")
        print(f">> Armor: {armor}")
    else:
        print("Access denied!")


################################################   Task Description   ################################################
# 2. Boss Rush
