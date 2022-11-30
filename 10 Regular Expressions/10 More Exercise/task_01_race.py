import re

participants = input().split(", ")
race_results = {}
info = input()
while info != "end of race":
    name_pattern = r"[A-Za-z]"
    distance_pattern = r"[0-9]"
    name_match = re.findall(name_pattern, info)
    distance_match = re.findall(distance_pattern, info)
    name = "".join(name_match)
    distance = sum([int(x) for x in distance_match])
    if name in participants:
        if name not in race_results:
            race_results[name] = distance
        else:
            race_results[name] += distance
    info = input()
sorted_results = dict(sorted(race_results.items(), key=lambda x: -x[1]))
rank = 0
for name in sorted_results:
    rank += 1
    if rank > 3:
        break
    if rank == 1:
        current_rank = "1st"
    elif rank == 2:
        current_rank = "2nd"
    elif rank == 3:
        current_rank = "3rd"
    print(f"{current_rank} place: {name}")


################################################   Task Description   ################################################
# 1. Race
# Write a program that processes information about a race.
# On the first line you will be given list of participants separated by ", ".
# On the next few lines until you receive a line "end of race" you will be given some info
# which will be some alphanumeric characters.
# In between them you could have some extra characters which you should ignore.
# For example: "G!32e%o7r#32g$235@!2e".
# The letters are the name of the person and the sum of the digits is the distance he ran.
# So here we have George who ran 29 km.
# Store the information about the person only if the list of racers contains the name of the person.
# If you receive the same person more than once just add the distance to his old distance.
# At the end print the top 3 racers ordered by distance in descending in the format:
#  "1st place: {first racer}
#   2nd place: {second racer}
#   3rd place: {third racer}"
