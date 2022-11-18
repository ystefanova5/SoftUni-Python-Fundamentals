import re

pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
text = input()
matched_numbers = re.finditer(pattern, text)
matched_numbers = [number.group() for number in matched_numbers]
print(*matched_numbers)


################################################   Task Description   ################################################
# 4. Match Numbers
# Write a program that finds all integer and floating-point numbers in a string.
