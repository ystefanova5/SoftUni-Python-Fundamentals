neighbourhood = list(map(int, input().split("@")))
command = input()
house_index = 0
while command != "Love!":
    length = int(command.split()[1])
    house_index += length
    if house_index >= len(neighbourhood):
        house_index = 0
    if neighbourhood[house_index] == 0:
        print(f"Place {house_index} already had Valentine's day.")
    else:
        neighbourhood[house_index] -= 2
        if neighbourhood[house_index] == 0:
            print(f"Place {house_index} has Valentine's day.")
    command = input()
print(f"Cupid's last position was {house_index}.")
if sum(neighbourhood) == 0:
    print("Mission was successful.")
else:
    house_count = 0
    for house in neighbourhood:
        if house != 0:
            house_count += 1
    print(f"Cupid has failed {house_count} places.")
