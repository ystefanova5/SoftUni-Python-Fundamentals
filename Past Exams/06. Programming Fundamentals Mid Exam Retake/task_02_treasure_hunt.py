def drop(list_name, index):
    if index in range(len(list_name)) or abs(index) <= len(list_name):
        treasure = list_name.pop(index)
        list_name.append(treasure)
    return list_name


def steal(list_name, count):
    stolen = []
    if count >= len(list_name):
        stolen = list_name.copy()
        list_name.clear()
    else:
        for i in range(count):
            stolen += [list_name.pop()]
        stolen.reverse()
    return list_name, stolen


treasure_chest = input().split("|")
command = input()
while command != "Yohoho!":
    current_action = command.split()[0]
    if current_action == "Loot":
        treasures = command.split()
        treasures.remove("Loot")
        for item in treasures:
            if item not in treasure_chest:
                treasure_chest.insert(0, item)
    elif current_action == "Drop":
        current_index = int(command.split()[1])
        treasure_chest = drop(treasure_chest, current_index)
    elif current_action == "Steal":
        stolen_items = []
        current_item = int(command.split()[1])
        treasure_chest, stolen_items = steal(treasure_chest, current_item)
        if len(stolen_items) > 0:
            print(", ".join(stolen_items))
    command = input()

treasure_length = 0
average_gain = 0
if len(treasure_chest) > 0:
    for treasure in treasure_chest:
        treasure_length += len(treasure)
    average_gain = treasure_length / len(treasure_chest)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")
