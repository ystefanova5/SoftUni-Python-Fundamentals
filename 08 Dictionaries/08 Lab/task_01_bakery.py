# 01. Bakery
# Task Description:
# You will receive a single line containing some food (keys) and quantities (values). 
# They will be separated by a single space (the first element is the key, the second – the value, and so on). 
# Create a dictionary with all the keys and values and print it on the console.


items = input().split()
keys = [key for key in items if items.index(key) % 2 == 0]
values = [int(value) for value in items if items.index(value) % 2 != 0]
bakery_dict = dict(zip(keys, values))
print(bakery_dict)
