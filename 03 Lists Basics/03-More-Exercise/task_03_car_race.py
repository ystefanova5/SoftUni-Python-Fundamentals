numbers_sequence = input()
sequence_list = numbers_sequence.split(" ")
sequence_list = [int(i) for i in sequence_list]
middle_index = int(len(sequence_list) / 2)
left_car_time = float()
right_car_time = float()
for left_index in range(middle_index):
    current_left_time = sequence_list[left_index]
    if current_left_time == 0:
        left_car_time *= 0.80
    else:
        left_car_time += current_left_time
sequence_list.reverse()
for right_index in range(middle_index):
    current_right_time = sequence_list[right_index]
    if current_right_time == 0:
        right_car_time *= 0.80
    else:
        right_car_time += current_right_time
if left_car_time < right_car_time:
    winner = "left"
    winner_time = left_car_time
else:
    winner = "right"
    winner_time = right_car_time
print(f"The winner is {winner} with total time: {winner_time:.1f}")


################################################   Task Description   ################################################
# 3. Car Race
# Write a program that announces the winner of a car race. 
# You will receive a sequence of numbers. 
# Each number represents the time the car needs to pass through that step (the index). 
# There will be two cars. The first one starts from the left side, and the other one starts from the right side. 
# The middle index of the sequence is the finish line. 
# Calculate the total time each racer needs to reach the finish line 
# and print the winner with his total time (the racer with less time). 
# If you have a zero in the list, you should reduce the racer's time that reached it by 20% (from his current time).
# The number of elements in the sequence will always be odd.
# Print the result in the following format "The winner is {left/right} with total time: {total_time}".
