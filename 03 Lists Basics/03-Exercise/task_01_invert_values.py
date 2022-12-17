input_string = input()
first_list = input_string.split(" ")
second_list = []
for i in range(len(first_list)):
    new_value = int(first_list[i]) * -1
    second_list.append(new_value)
print(second_list)


################################################   Task Description   ################################################
# 1. Invert Values
# Write a program that receives a single string containing positive and negative numbers separated by a single space. 
# Print a list containing the opposite of each number.
