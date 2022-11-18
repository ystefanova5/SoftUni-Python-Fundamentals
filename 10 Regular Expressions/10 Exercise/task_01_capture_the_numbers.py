import re

text = input()
while text:
    pattern = r"\d+"
    match = re.findall(pattern, text)
    if match:
        print(*match, end=" ")
    text = input()


################################################   Task Description   ################################################
# 1. Capture the Numbers
# Write a program that receives strings on different lines and extracts only the numbers.
# Print all extracted numbers on a single line, separated by a single space.
