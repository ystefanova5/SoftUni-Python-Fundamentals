import re

pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
text = input()
validated_names = re.findall(pattern, text)
print(" ".join(validated_names))


################################################   Task Description   ################################################
# 1. Match Full Name
# Write a program to match full names from a sequence of characters and print them on the console.
