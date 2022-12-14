number = int(input())
number_is_prime = True
for n in range(2, number):
    if number % n == 0:
        number_is_prime = False
        break
print(number_is_prime)


################################################   Task Description   ################################################
# 2. Prime Number Checker
# Write a program to check if a number is prime. 
# A prime number is a natural number greater than 1, not a product of two smaller natural numbers. 
# For example, the only ways of writing 5 as a product, 1 × 5 or 5 × 1, involve 5 itself.
# The input comes as an integer number.
# The output should be True if the number is prime and False otherwise.
