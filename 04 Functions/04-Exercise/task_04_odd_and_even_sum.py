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


################################################   Task Description   ################################################
# 4. Odd and Even Sum
# You will receive a single number. You should write a function that returns the sum 
# of all even and all odd digits in a given number. The result should be returned as a single string in the format: 
# "Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"
# Print the result of the function on the console.
