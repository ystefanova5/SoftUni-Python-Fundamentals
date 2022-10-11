def find_perfect_number(number):
    divisor_list = []
    for divisor in range(1, number):
        if number % divisor == 0:
            divisor_list.append(divisor)
    if sum(divisor_list) == number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


current_number = int(input())
print(find_perfect_number(current_number))
