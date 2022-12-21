def check_even_numbers(number):
    if number % 2 == 0:
        return True
    else:
        return False


numbers_list = list(map(int, input().split(" ")))
even_nums_filtering = filter(check_even_numbers, numbers_list)
even_nums = list(even_nums_filtering)
print(even_nums)


################################################   Task Description   ################################################
# 5. Even Numbers
# Write a program that receives a sequence of numbers (integers) separated by a single space. 
# It should print a list of only the even numbers. Use filter().
