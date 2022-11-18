import re

pattern = r"(\+359 2 \d{3} \d{4}\b)|(\+359-2-\d{3}-\d{4}\b)"
numbers = input()
matched_numbers = re.finditer(pattern, numbers)
valid_numbers = [x.group() for x in matched_numbers]
print(", ".join(valid_numbers))


################################################   Task Description   ################################################
# 2. Match Phone Number
# Write a regular expression to match a valid phone number from Sofia. 
# After you find all valid phones, print them on the console, separated by a comma and a space ", ".
