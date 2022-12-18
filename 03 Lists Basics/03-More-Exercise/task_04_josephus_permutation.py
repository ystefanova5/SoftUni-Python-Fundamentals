people_sequence = input()
execution_number = int(input())
people_list = people_sequence.split(" ")
people_list = [int(x) for x in people_list]
executions_list = []
kill_counter = 0
current_index = 0

while len(people_list) > 0:
    kill_counter += 1

    if current_index >= len(people_list):
        current_index = 0

    if kill_counter % execution_number == 0:
        executions_list.append(people_list[current_index])
        people_list.pop(current_index)
        # executions_list.append(people_list.pop(index))
    else:
        current_index += 1

print(str(executions_list).replace(" ", ""))


################################################   Task Description   ################################################
# 4. Josephus Permutation
# This problem takes its name from arguably the most important event in the life of the ancient historian Josephus. 
# According to his tale, he and his 40 soldiers were trapped in a cave by the Romans during a siege. 
# Refusing to surrender to the enemy, they instead opted for mass suicide, with a twist: 
# they formed a circle and proceeded to kill one man of every three until one last man was left 
# (and that it was supposed to kill himself to end the act). 
# Well, Josephus and another man were the last, and, as we now know every detail of the story, 
# you may have correctly guessed that they did not precisely follow through with the original idea.
# You are now to create a program that prints a Josephus permutation, receiving two lines of code:
#     • the list itself - numbers separated by a single space representing the people in the circle
#     • a number k
# People are standing in a circle waiting to be executed. 
# Counting begins from the first one in the circle and proceeds from left to right. 
# After a specified number of people are skipped, the k person is executed. 
# The procedure is repeated with the remaining people, starting with the next person, going in the same direction, 
# and skipping the same number of people until no one remains.
# Print the people by order of executions in the format: "[{executed1},{executed2}, … {executedN}]"
