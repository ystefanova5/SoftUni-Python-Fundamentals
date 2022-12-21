def get_smallest_number(number01, number02, number03):
    numbers_list = [number01, number02, number03]
    return min(numbers_list)


first_number, second_number, third_number = int(input()), int(input()), int(input())
print(get_smallest_number(first_number, second_number, third_number))


################################################   Task Description   ################################################
# 1. Smallest of Three Numbers
# Write a function that receives three integer numbers and returns the smallest. 
# Print the result on the console. Use an appropriate name for the function.
