input_integers = input()
count_to_remove = int(input())
strings_list = input_integers.split(" ")
integers_list = ([int(x) for x in strings_list])
for i in range(count_to_remove):
    integers_list.remove(min(integers_list))
for j in range(len(integers_list)):
    if j == 0:
        print(integers_list[j], end="")
    else:
        print(f", {integers_list[j]}", end="")


################################################   Task Description   ################################################
# 6. Survival of the Biggest
# Write a program that receives a list of integer numbers (separated by a single space) and a number n. 
# The number n represents the count of numbers to remove from the list. 
# You should remove the smallest ones, and then, you should print all the numbers that are left in the list, 
# separated by a comma and a space ", ".
