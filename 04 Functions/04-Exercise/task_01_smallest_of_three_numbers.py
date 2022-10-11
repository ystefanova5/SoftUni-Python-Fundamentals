def get_smallest_number(number01, number02, number03):
    numbers_list = [number01, number02, number03]
    return min(numbers_list)


first_number, second_number, third_number = int(input()), int(input()), int(input())
print(get_smallest_number(first_number, second_number, third_number))
