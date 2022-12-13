number_of_characters = int(input())
sum_of_characters = 0
for i in range(number_of_characters):
    current_character = input()
    sum_of_characters += ord(current_character)
print(f"The sum equals: {sum_of_characters}")


################################################   Task Description   ################################################
# 4. Sum of Chars
# Write a program, which sums the ASCII codes of N characters and prints the sum on the console. 
# On the first line, you will receive N – the number of lines. 
# On the following N lines – you will receive a letter per line. 
# Print the total sum in the following format: "The sum equals: {total_sum}".
# Note: n will be in the interval [1…20].
