factor = int(input())
count = int(input())
output_list = [factor]
current_number = factor
for i in range(count - 1):
    current_number += factor
    output_list.append(current_number)
print(output_list)


################################################   Task Description   ################################################
# 2. Multiples List
# Write a program that receives two numbers (factor and count). 
# It should create a list with a length of the given count that contains only integer numbers, 
# which are multiples of the given factor. 
# The numbers should be only positive, and they should be arranged in ascending order, 
# starting from the value of the factor.
