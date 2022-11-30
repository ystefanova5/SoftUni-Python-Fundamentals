def fire(ship_name, index, damage):
    message = None
    if index in range(len(ship_name)) and abs(index) <= len(ship_name):
        ship_name[index] -= damage
        if ship_name[index] <= 0:
            message = "You won! The enemy ship has sunken."
    return ship_name, message


def defend(ship_name, start_index, end_index, damage):
    message = None
    if start_index in range(len(ship_name)) and abs(start_index) <= len(ship_name):
        if end_index in range(len(ship_name)) and abs(end_index) <= len(ship_name):
            if start_index < 0:
                start_index = ship_name.index(ship_name[start_index])
            if end_index < 0:
                end_index = ship_name.index(ship_name[end_index])
            if start_index <= end_index:
                for index in range(start_index, end_index + 1):
                    ship_name[index] -= damage
                    if ship_name[index] <= 0:
                        message = "You lost! The pirate ship has sunken."
                        break
    return ship_name, message


def repair(ship_name, index, health, treshold):
    if index in range(len(ship_name)) and abs(index) <= len(ship_name):
        ship_name[index] += health
        if ship_name[index] > treshold:
            ship_name[index] = treshold
    return ship_name


def status(ship_name, treshold):
    repair_treshold = treshold * 0.20
    count = 0
    for section in ship_name:
        if section < repair_treshold:
            count += 1
    return count


pirate_ship = list(map(int, input().split(">")))
warship = list(map(int, input().split(">")))
max_health = int(input())
ships_are_in_stalemate = True
command = input()
while command != "Retire":
    current_command = command.split()[0]
    if current_command == "Fire":
        fire_index = int(command.split()[1])
        fire_damage = int(command.split()[2])
        warship, fire_message = fire(warship, fire_index, fire_damage)
        if fire_message is not None:
            ships_are_in_stalemate = False
            print(fire_message)
            break
    elif current_command == "Defend":
        defend_start_index = int(command.split()[1])
        defend_end_index = int(command.split()[2])
        defend_damage = int(command.split()[3])
        pirate_ship, defend_message = defend(pirate_ship, defend_start_index, defend_end_index, defend_damage)
        if defend_message is not None:
            ships_are_in_stalemate = False
            print(defend_message)
            break
    elif current_command == "Repair":
        repair_index = int(command.split()[1])
        health = int(command.split()[2])
        pirate_ship = repair(pirate_ship, repair_index, health, max_health)
    elif current_command == "Status":
        repair_count = status(pirate_ship, max_health)
        print(f"{repair_count} sections need repair.")
    command = input()

if ships_are_in_stalemate:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(warship)}")
