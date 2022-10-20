groceries = input().split("!")
command = input()
while command != "Go Shopping!":
    command_type = command.split()[0]
    item = command.split()[1]
    if command_type == "Urgent":
        if item not in groceries:
            groceries.insert(0, item)
    elif command_type == "Unnecessary":
        if item in groceries:
            groceries.remove(item)
    elif command_type == "Correct":
        old_item = item
        new_item = command.split()[2]
        if old_item in groceries:
            index = groceries.index(old_item)
            groceries[index] = new_item
    elif command_type == "Rearrange":
        if item in groceries:
            groceries.remove(item)
            groceries.append(item)
    command = input()
print(", ".join(groceries))
