def sum_numbers(number01, number02):
    return number01 + number02


def subtract(sum, number03):
    return sum - number03


def add_and_subtract(number01, number02, number03):
    sum_of_numbers = sum_numbers(number01, number02)
    return subtract(sum_of_numbers, number03)


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(add_and_subtract(first_number, second_number, third_number))


################################################   Task Description   ################################################
# 2. Add and Subtract
# You will receive three integer numbers. 
# Write functions named:
#     • sum_numbers() that returns the sum of the first two integers
#     • subtract() that returns the difference between the returned result of the first function and the third integer
# Wrap the two functions in a function named add_and_subtract() which will receive the three numbers as parameters. 
# Print the result of the subtract() function on the console.
