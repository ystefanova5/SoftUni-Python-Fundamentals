team_a_count = 11
team_b_count = 11
cards_list = input().split(" ")
cards_list = list(dict.fromkeys(cards_list))
game_was_terminated = False
for i in range(len(cards_list)):
    current_player = cards_list[i]
    if current_player[0] == "A":
        team_a_count -= 1
    elif current_player[0] == "B":
        team_b_count -= 1
    if team_a_count < 7 or team_b_count < 7:
        game_was_terminated = True
        break
print(f"Team A - {team_a_count}; Team B - {team_b_count}")
if game_was_terminated:
    print("Game was terminated")


################################################   Task Description   ################################################
# 3. Football Cards
# Most football fans love it for the goals and excitement. Well, this problem does not. 
# You are up to handle the referee's little notebook and count the players who were sent off for fouls and misbehavior.
# The rules: Two teams, named "A" and "B" have 11 players each. The players on each team are numbered from 1 to 11. 
# Any player may be sent off the field by being given a red card. 
# If one of the teams has less than 7 players remaining, the referee stops the game immediately, 
# and the team with less than 7 players loses.
# The card is a string with the team's letter ("A" or "B") followed by a single dash and the player's number. 
# e.g., the card "B-7" means player #7 from team B received a card.
# The task: You will be given a sequence of cards (could be empty), separated by a single space. 
# You should print the count of remaining players on each team at the end of the game in the format: 
# "Team A - {players_count}; Team B - {players_count}". 
# If the referee terminated the game, print an additional line: "Game was terminated".
# Note for the random tests: If a player who has already been sent off receives another card - ignore it.

