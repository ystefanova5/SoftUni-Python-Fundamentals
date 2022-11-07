users = {}
contests = {}
input_line = input().split(" -> ")
while input_line[0] != "no more time":
    username, contest, points = input_line[0], input_line[1], int(input_line[2])
    if contest not in contests:
        contests[contest] = {username: 0}
    if username not in contests[contest]:
        contests[contest][username] = 0
    else:
        if points < contests[contest][username]:
            points = contests[contest][username]
    contests[contest][username] = points
    contests[contest][username] = points
    if username not in users:
        users[username] = {"total_points": 0, contest: 0}
    if contest not in users[username]:
        users[username][contest] = 0
    else:
        users[username]["total_points"] -= users[username][contest]
        if points < users[username][contest]:
            points = users[username][contest]
    users[username]["total_points"] += points
    users[username][contest] = points
    input_line = input().split(" -> ")

for contest in contests:
    print(f"{contest}: {len(contests[contest])} participants")
    sorted_participants = sorted(contests[contest].items(), key=lambda x: (-x[1], x[0]))
    sorted_contest = dict(sorted_participants)
    counter = 0
    for participant, points in sorted_contest.items():
        counter += 1
        print(f"{counter}. {participant} <::> {points}")

new_keys = []
new_values = []
for key, value in users.items():
    new_keys.append(key)
    new_values.append(value["total_points"])
user_scores = dict(zip(new_keys, new_values))
sorted_scores = dict(sorted(user_scores.items(), key=lambda k: (-k[1], k[0])))
print("Individual standings:")
counter = 0
for key, value in sorted_scores.items():
    counter += 1
    print(f"{counter}. {key} -> {value}")


################################ Task Description ################################
# 2. Judge
# You know the judge system, right?! Your job is to create a program similar to the Judge system.
# You will receive several input lines in one of the following formats:
# "{username} -> {contest} -> {points}"
# The "contest" and "username" are strings, the given "points" will be an integer number.
# You need to keep track of every contest and points of each user:
# • If the user has already participated in the contest,
# update their points only if the new ones are more than the older ones.
# • Otherwise, just save the data - contest, username, and points.
# Also, you need to keep individual statistics for each user - his/her final total points for all contests.
# You should end your program when you receive the command "no more time".
# At that point, you should print each contest in order of input, for each contest
# print the participants ordered by points in descending order, then ordered by name in ascending order.
# After that, you should print individual statistics for every participant ordered by total points in descending order,
# and then by alphabetical order.
# Input / Constraints
# • The input comes in the form of commands in one of the formats specified above.
# • Username and contest name always will be one word.
# • Points will be an integer in the range [0, 1000].
# • There will be no invalid input lines.
# • If all sorting criteria fail, the order should be by order of input.
# • The input ends when you receive the command "no more time".
# Output
# • The output format for the contests is:
# "{constest_name}: {number_participants} participants
# 1. {username1} <::> {points}
# 2. {username2} <::> {points}
# …
# {N}. {usernameN} <::> {points}"
# • After you print all contests, print the individual statistics for every participant.
# • The output format is:
# "Individual standings:
# 1. {username1} -> {total_points}
# 2. {username} -> {total_points}
# …
# {N}. {username} -> {total_points}"
