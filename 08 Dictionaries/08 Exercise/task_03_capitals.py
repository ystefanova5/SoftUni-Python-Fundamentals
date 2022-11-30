countries = input().split(", ")
capitals = input().split(", ")
capitals_dict = dict(zip(countries, capitals))
for key, value in capitals_dict.items():
    print(f"{key} -> {value}")
    

################################################   Task Description   ################################################
# 3. Capitals
# Using a dictionary comprehension, write a program that receives country names on the first line,
# separated by comma and space ", ", and their corresponding capital cities on the second line
# (again separated by comma and space ", ").
# Print each country with their capital on a separate line in the following format: "{country} -> {capital}".
