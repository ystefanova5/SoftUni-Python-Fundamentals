divisor = int(input())
boundary = int(input())
largest_possible_num = int()
for number in range(1, boundary + 1):
    if (number > 0) and (number % divisor == 0) and (number <= boundary):
        largest_possible_num = number
    else:
        continue
print(largest_possible_num)