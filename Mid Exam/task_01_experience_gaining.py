needed_experience = float(input())
battles = int(input())
gained_experience = 0
actual_battles = 0

for battle in range(1, battles + 1):
    actual_battles += 1
    current_experience = float(input())
    gained_experience += current_experience
    if current_experience != 0:
        if battle % 15 == 0:
            gained_experience += current_experience * 0.05
        else:
            if battle % 3 == 0:
                gained_experience += current_experience * 0.15
            if battle % 5 == 0:
                gained_experience -= current_experience * 0.10
    if gained_experience >= needed_experience:
        break


difference = abs(needed_experience - gained_experience)
if gained_experience >= needed_experience:
    print(f"Player successfully collected his needed experience for {actual_battles} battles.")
else:
    print(f"Player was not able to collect the needed experience, {difference:.2f} more needed.")
