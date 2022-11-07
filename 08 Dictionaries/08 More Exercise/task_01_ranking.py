contest_validation = {}
contest_participants = {}
line = input()
while line != "end of contests":
    current_contest = line.split(":")[0]
    current_password = line.split(":")[1]
    contest_validation[current_contest] = current_password
    line = input()
submission = input()
while submission != "end of submissions":
    contest = submission.split("=>")[0]
    password = submission.split("=>")[1]
    username = submission.split("=>")[2]
    points = int(submission.split("=>")[3])
    if contest in contest_validation and contest_validation[contest] == password:
        if username not in contest_participants:
            contest_participants[username] = {"total_points": 0, contest: 0}
        else:
            if contest in contest_participants[username]:
                contest_participants[username]["total_points"] -= contest_participants[username][contest]
                if contest_participants[username][contest] > points:
                    points = contest_participants[username][contest]
            else:
                contest_participants[username][contest] = 0
        contest_participants[username][contest] = points
        contest_participants[username]["total_points"] += points
    submission = input()
max_points = -1
best_candidate = ""
for candidate in contest_participants:
    if contest_participants[candidate]["total_points"] > max_points:
        best_candidate = candidate
        max_points = contest_participants[candidate]["total_points"]
print(f"Best candidate is {best_candidate} with total {max_points} points.")
print("Ranking:")
sorted_names = sorted(contest_participants)
sorted_participants = {key: contest_participants[key] for key in sorted_names}
for participant, exam_results in sorted_participants.items():
    print(participant)
    sorted_results = {key: value for key, value in sorted(exam_results.items(), key=lambda item: item[1], reverse=True)}
    for exam, points in sorted_results.items():
        if exam != "total_points":
            print(f"#  {exam} -> {points}")

################################ Task Description ################################
# 1. Ranking
# Here comes the final and the most interesting part – the Final ranking of the candidate-interns.
# The final ranking is determined by the points of the interview tasks and by the points from the exams in SoftUni.
# Here is your final task. You will receive some lines of input in the format "{contest}:{password for contest}"
# until you receive "end of contests". Save that data because you will need it later.
# After that you will receive other type of inputs in format "{contest}=>{password}=>{username}=>{points}"
# until you receive "end of submissions". Here is what you need to do.
# • Check if the contest is valid (It is considered valid if you received it in the first type of input)
# • Check if the password is correct for the given contest
# • If the contest and the password is valid, save the user with the contest they take part in
# (a user can take part in many contests) and the points the user has in the given contest.
# If you receive the same contest and the same user update the points only if the new ones are more than the older ones.
# In the end, you should print the info for the user with the most points
# (total points for all contents they participated in) in the format
# "Best candidate is {user} with total {total_points} points.".
# After that print all students ordered by their names.
# For each user print each contest with the points in descending order. See the examples.
# Input
# • Strings in format "{contest}:{password for contest}" until the "end of contests" command.
#   There will be no case with two equal contests
# • Strings in format "{contest}=>{password}=>{username}=>{points}" until the "end of submissions" command.
# • There will be no case with 2 or more users with same total points!
# Output
# • On the first line, print the best user in format "Best candidate is {user} with total {total points} points.".
# • Then print all students ordered as mentioned above in format:
# "{user_name1}
# #  {contest1} -> {points}
# #  {contest2} -> {points}
# …
# #  {contestN} -> {points}"
# Constraints
# • The strings may contain any ASCII character except from (:, =, >).
# • The numbers will be in range [0 - 10000].
# • Second input is always valid.
