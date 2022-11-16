exam_results = {}
banned = []
command = input()
while command != "exam finished":
    current_submission = command.split("-")
    if len(current_submission) == 2:
        current_username = current_submission[0]
        banned.append(current_username)
    else:
        current_username, current_language = current_submission[0], current_submission[1]
        current_points = int(current_submission[2])
        if current_language not in exam_results:
            exam_results[current_language] = {"submissions": 0}
        if current_username in exam_results[current_language]:
            if exam_results[current_language][current_username] > current_points:
                current_points = exam_results[current_language][current_username]
        exam_results[current_language][current_username] = current_points
        exam_results[current_language]["submissions"] += 1
    command = input()
print("Results:")
for value in exam_results.values():
    for person, points in value.items():
        if person not in banned and person != "submissions":
            print(f"{person} | {points}")
print("Submissions:")
for value, key in exam_results.items():
    print(f"{value} - {exam_results[value]['submissions']}")

    
################################################   Task Description   ################################################
# 12. SoftUni Exam Results
# Judge statistics on the last Programing Fundamentals exam were not working correctly,
# so you have the task of taking all the submissions and analyzing them properly.
# You should collect all the submissions and print the final results and statistics about each language
# in which the participants submitted their solutions.
# You will be receiving lines in the following format: "{username}-{language}-{points}"
# until you receive "exam finished". You should store each username and their submissions and points.
# If a student has two or more submissions for the same language, save only his maximum points.
# You can receive a command to ban a user for cheating in the following format: "{username}-banned".
# In that case, you should remove the user from the contest but preserve his submissions
# in the total count of submissions for each language.
# After receiving "exam finished", print each of the participants in the following format:
# "Results:
# {username1} | {points}
# {username2} | {points}
# …
# {usernameN} | {points}"
# After that, print each language used in the exam in the following format:
# "Submissions:
# {language1} - {submissions_count}
# {language2} - {submissions_count}
# …
# {language3} - {submissions_count}"
# Input / Constraints
# Until you receive "exam finished" you will be receiving participant submissions in the following format:
# "{username}-{language}-{points}"
# You can receive a ban command -> "{username}-banned"
# The points of the participant will always be a valid integer in the range [0-100];
# Output
# • Print the exam results for each participant
# • After that, print each language in the format shown above
# • Allowed working time / memory: 100ms / 16MB
