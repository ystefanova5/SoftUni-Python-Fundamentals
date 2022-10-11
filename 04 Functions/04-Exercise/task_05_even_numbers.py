def check_even_numbers(number):
    if number % 2 == 0:
        return True
    else:
        return False


numbers_list = list(map(int, input().split(" ")))
even_nums_filtering = filter(check_even_numbers, numbers_list)
even_nums = list(even_nums_filtering)
print(even_nums)
