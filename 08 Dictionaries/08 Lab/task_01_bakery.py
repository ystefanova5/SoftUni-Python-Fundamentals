items = input().split()
keys = [key for key in items if items.index(key) % 2 == 0]
values = [int(value) for value in items if items.index(value) % 2 != 0]
bakery_dict = dict(zip(keys, values))
print(bakery_dict)