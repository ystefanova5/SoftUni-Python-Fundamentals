tour_stops = input()
command = input()
while command != "Travel":
    action = command.split(":")[0]
    if action == "Add Stop":
        index, string = int(command.split(":")[1]), command.split(":")[2]
        if index in range(len(tour_stops)):
            tour_stops = tour_stops[:index] + string + tour_stops[index:]
    elif action == "Remove Stop":
        start_index, end_index = int(command.split(":")[1]), int(command.split(":")[2])
        if start_index in range(len(tour_stops)) and end_index in range(len(tour_stops)):
            tour_stops = tour_stops[:start_index] + tour_stops[end_index + 1:]
    elif action == "Switch":
        old_string, new_string = command.split(":")[1], command.split(":")[2]
        if old_string in tour_stops:
            tour_stops = tour_stops.replace(old_string, new_string)
    print(tour_stops)
    command = input()
print(f"Ready for world tour! Planned stops: {tour_stops}")


################################################   Task Description   ################################################
# Problem 1 - World Tour
# 
# Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
# Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2518#0.
# 
# You are a world traveler, and your next goal is to make a world tour. To do that, you have to plan out everything first. 
# To start with, you would like to plan out all of your stops where you will have a break.
# On the first line, you will be given a string containing all of your stops. 
# Until you receive the command "Travel", you will be given some commands to manipulate that initial string. 
# The commands can be:
# • "Add Stop:{index}:{string}":
#     o Insert the given string at that index only if the index is valid
# • "Remove Stop:{start_index}:{end_index}":
#     o Remove the elements of the string from the starting index to the end index (inclusive) if both indices are valid
# • "Switch:{old_string}:{new_string}":
#     o If the old string is in the initial string, replace it with the new one (all occurrences)
# Note: After each command, print the current state of the string if it is valid!
# After the "Travel" command, print the following: "Ready for world tour! Planned stops: {string}"
# Input / Constraints
# • JavaScript: you will receive a list of strings
# • An index is valid if it is between the first and the last element index (inclusive) (0 ….. Nth) in the sequence.
# Output
# • Print the proper output messages in the proper cases as described in the problem description
