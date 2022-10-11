def odd_even_num(digit):
    if digit % 2 == 0:
        return "Even"
    else:
        return "Odd"


def odd_even_sum(number):
    sum_odd = 0
    sum_even = 0
    digits_list = [int(x) for x in str(number)]
    for current_digit in digits_list:
        if odd_even_num(current_digit) == "Odd":
            sum_odd += current_digit
        elif odd_even_num(current_digit) == "Even":
            sum_even += current_digit
    return f"Odd sum = {sum_odd}, Even sum = {sum_even}"


input_number = int(input())
print(odd_even_sum(input_number))
