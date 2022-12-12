range_number = int(input())
for number in range(1, range_number + 1):
    number_string = str(number)
    status = False
    sum_numbers = 0
    for character in number_string:
        sum_numbers += int(character)
    if sum_numbers in [5, 7, 11]:
        status = True
    print(f"{number} -> {status}")


################################################   Task Description   ################################################
# 3. Special Numbers
# Write a program that reads an integer n. 
# Then, for all numbers in the range [1, n], prints the number and if it is special or not (True / False). 
# A number is special when the sum of its digits is 5, 7, or 11.
