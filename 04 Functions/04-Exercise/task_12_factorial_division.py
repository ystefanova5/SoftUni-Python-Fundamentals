def calculate_factorial(number):
    factorial_result = 1
    for current_number in range(1, number + 1):
        factorial_result *= current_number
    return factorial_result


first_number = int(input())
second_number = int(input())
result = calculate_factorial(first_number) / calculate_factorial(second_number)
print(f"{result:.2f}")


################################################   Task Description   ################################################
# 12. * Factorial Division
# Write a function that receives two integer numbers. Calculate the factorial of each number. 
# Divide the first result by the second and print the division formatted to the second decimal point.
