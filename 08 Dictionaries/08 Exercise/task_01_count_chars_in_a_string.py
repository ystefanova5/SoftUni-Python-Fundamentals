chars_string = input()
chars_dict = {}
for char in chars_string:
    if char != " ":
        if char not in chars_dict:
            chars_dict[char] = 0
        chars_dict[char] += 1
for key, value in chars_dict.items():
    print(f"{key} -> {value}")


################################################   Task Description   ################################################
# 1. Count Chars in a String
# Write a program that counts all characters in a string except for space (" ").
# Print all the occurrences in the following format:
# "{char} -> {occurrences}"
