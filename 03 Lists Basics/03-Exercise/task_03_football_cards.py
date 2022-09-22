team_A_count = 11
team_B_count = 11
cards = input()
cards_list = cards.split(" ")
cards_list = list(dict.fromkeys(cards_list))
for i in range(len(cards_list)):
    current_player = cards_list[i]
    if current_player[0] == "A":
        team_A_count -= 1
    elif current_player[0] == "B":
        team_B_count -= 1
    if team_A_count < 7 or team_B_count < 7:
        break
print(f"Team A - {team_A_count}; Team B - {team_B_count}")
if team_A_count < 7 or team_B_count < 7:
    print("Game was terminated")