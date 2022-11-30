energy = int(input())
won_battles = 0
energy_is_enough = True
command = input()
while command != "End of battle":
    distance = int(command)
    if distance <= energy:
        energy -= distance
        won_battles += 1
    else:
        energy_is_enough = False
        print(f"Not enough energy! Game ends with {won_battles} won battles and {energy} energy")
        break
    if won_battles % 3 == 0:
        energy += won_battles
    command = input()
if energy_is_enough:
    print(f"Won battles: {won_battles}. Energy left: {energy}")
