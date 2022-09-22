decorations_quantity = int(input())
days_until_christmas = int(input())
budget = 0
total_spirit = 0
for days in range(1, days_until_christmas + 1):
    if days % 11 == 0:
        decorations_quantity += 2
    if days % 2 == 0:
        budget += decorations_quantity * 2
        total_spirit += 5
    if days % 3 == 0:
        budget += decorations_quantity * (5 + 3)
        total_spirit += 3 + 10
    if days % 5 == 0:
        budget += decorations_quantity * 15
        total_spirit += 17
    if days % 3 == 0 and days % 5 == 0:
        total_spirit += 30
    if days % 10 == 0:
        total_spirit -= 20
        budget += 5 + 3 + 15
if days_until_christmas % 10 == 0:
    total_spirit -= 30
print(f"Total cost: {budget:.0f}")
print(f"Total spirit: {total_spirit}")
