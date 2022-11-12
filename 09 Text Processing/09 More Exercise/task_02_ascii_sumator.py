first_character = ord(input())
second_character = ord(input())
sum_of_characters = 0
some_string = input()
for symbol in some_string:
    if first_character < ord(symbol) < second_character:
        sum_of_characters += ord(symbol)
print(sum_of_characters)


################################################   Task Description   ################################################
# 2. ASCII Sumator
# Write a program that prints the sum of all found characters between two given characters (their ASCII code).
# On each of the first two lines, you will receive a single character. On the last line, you get a random string.
# Print the sum of the ASCII values of all characters in the random string
# between the two given characters in the ASCII table.
