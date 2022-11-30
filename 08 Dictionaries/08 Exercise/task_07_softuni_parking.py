def register(username, license_plate_number, users):
    if username in users:
        return f"ERROR: already registered with plate number {license_plate_number}"
    else:
        users[username] = license_plate_number
        return f"{username} registered {license_plate_number} successfully"


def unregister(username, users):
    if username not in users:
        return f"ERROR: user {username} not found"
    else:
        del users[username]
        return f"{username} unregistered successfully"


parking_users = {}
number_of_commands = int(input())
for command in range(number_of_commands):
    current_command = input().split()
    current_task = current_command[0]
    current_username = current_command[1]
    if current_task == "register":
        current_license_plate = current_command[2]
        print(register(current_username, current_license_plate, parking_users))
    elif current_task == "unregister":
        print(unregister(current_username, parking_users))
for user in parking_users:
    print(f"{user} => {parking_users[user]}")


################################################   Task Description   ################################################
# 7. SoftUni Parking
# Write a program, which validates a parking place - users can register to enter the park and unregister to leave.
# The program receives 2 types of commands:
# • "register {username} {license_plate_number}":
#   o The system only supports one car per user at the moment,
#   so if a user tries to register another license plate using the same username, the system should print:
# "ERROR: already registered with plate number {license_plate_number}"
#   o If the check above passes successfully, the user should be registered, so the system should print:
#   "{username} registered {license_plate_number} successfully"
# • "unregister {username}":
#   o If the user is not present in the database, the system should print:
# "ERROR: user {username} not found"
#   o If the check above passes successfully, the system should print:
# "{username} unregistered successfully"
# After you execute all of the commands,
# print all the currently registered users and their license plates in the format:
# • "{username} => {license_plate_number}"
# Input
# • First line: n - number of commands - integer
# • Next n lines: commands in one of the two possible formats:
#   o Register: "register {username} {license_plate_number}"
#   o Unregister: "unregister {username}"
# The input will always be valid, and you do not need to check it explicitly.
