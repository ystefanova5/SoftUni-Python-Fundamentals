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


################################################   Task Description   ################################################
# 10. Perfect Number 
# A perfect number is a positive integer that is equal to the sum of its proper positive divisors. 
# That is the sum of its positive divisors, excluding the number itself (also known as its aliquot sum).
# Write a function that receives an integer number and returns one of the following messages:
#     • "We have a perfect number!" - if the number is perfect.
#     • "It's not so perfect." - if the number is NOT perfect.
# Print the result on the console.
