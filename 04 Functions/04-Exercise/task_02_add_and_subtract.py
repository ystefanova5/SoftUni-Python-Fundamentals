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
