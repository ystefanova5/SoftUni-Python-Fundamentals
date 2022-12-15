number = int(input())
numbers_list = []
filtered_list = []
for _ in range(number):
    current_number = int(input())
    numbers_list.append(current_number)
command = input()
if command == "even":
    for n in numbers_list:
        if n % 2 == 0:
            filtered_list.append(n)
elif command == "odd":
    for n in numbers_list:
        if n % 2 != 0:
            filtered_list.append(n)
elif command == "negative":
    for n in numbers_list:
        if n < 0:
            filtered_list.append(n)
elif command == "positive":
    for n in numbers_list:
        if n >= 0:
            filtered_list.append(n)
print(filtered_list)


################################################   Task Description   ################################################
# 5. Numbers Filter
# On the first line, you will receive a single number n. On the following n lines, you will receive integers. 
# After that, you will be given one of the following commands:
#     • even
#     • odd
#     • negative
#     • positive
# Filter all the numbers that fit in the category (0 counts as a positive and even). Finally, print the result.
