first_number = int(input())
second_number = int(input())
print("Before:")
print(f"a = {first_number}")
print(f"b = {second_number}")
first_number, second_number = second_number, first_number
print("After:")
print(f"a = {first_number}")
print(f"b = {second_number}")


################################################   Task Description   ################################################
# 1. Exchange Integers
# Read two integer numbers and, after that, exchange their values. 
# Print the variable values before and after the exchange.
