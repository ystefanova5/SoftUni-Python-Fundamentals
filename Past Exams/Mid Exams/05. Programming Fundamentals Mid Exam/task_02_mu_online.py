health = 100
bitcoins = 0
dungeon = input().split("|")
player_is_alive = True
best_room = 0
for room in dungeon:
    best_room += 1
    room_type = room.split()[0]
    room_value = int(room.split()[1])
    if room_type == "potion":
        healed_amount = 0
        if health < 100:
            health_needed = 100 - health
            if health_needed <= room_value:
                health = 100
                healed_amount = health_needed
            else:
                health += room_value
                healed_amount = room_value
        print(f"You healed for {healed_amount} hp.")
        print(f"Current health: {health} hp.")
    elif room_type == "chest":
        bitcoins += room_value
        print(f"You found {room_value} bitcoins.")
    else:
        health -= room_value
        if health > 0:
            print(f"You slayed {room_type}.")
        else:
            print(f"You died! Killed by {room_type}.")
            print(f"Best room: {best_room}")
            player_is_alive = False
            break
if player_is_alive:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
