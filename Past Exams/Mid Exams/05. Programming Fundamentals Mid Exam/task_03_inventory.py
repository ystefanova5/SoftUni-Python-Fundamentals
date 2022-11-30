def collect(list_name, item_name):
    if item_name not in list_name:
        list_name.append(item)
    return list_name


def drop(list_name, item_name):
    if item_name in list_name:
        list_name.remove(item_name)
    return list_name


def combine_items(list_name, old_item, new_item):
    if old_item in list_name:
        index_old = list_name.index(old_item)
        list_name.insert(index_old + 1, new_item)
    return list_name


def renew(list_name, item_name):
    if item_name in list_name:
        list_name.remove(item_name)
        list_name.append(item_name)
    return list_name


collecting_items = input().split(", ")
command = input()
while command != "Craft!":
    current_command = command.split(" - ")[0]
    command_body = command.split(" - ")[1]
    if current_command == "Collect":
        item = command_body
        collecting_items = collect(collecting_items, item)
    elif current_command == "Drop":
        item = command_body
        collecting_items = drop(collecting_items, item)
    elif current_command == "Combine Items":
        old = command_body.split(":")[0]
        new = command_body.split(":")[1]
        collecting_items = combine_items(collecting_items, old, new)
    elif current_command == "Renew":
        item = command_body
        collecting_items = renew(collecting_items, item)
    command = input()
print(", ".join(collecting_items))
