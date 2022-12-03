import re

text = input()
emoji_pattern = r"([\:\*])\1([A-Z][a-z]{2,})\1\1"
emoji_matches = re.finditer(emoji_pattern, text)
emojis = [x.group() for x in emoji_matches]
cool_pattern = r"\d"
cool_matches = re.findall(cool_pattern, text)
threshold_nums = [int(match) for match in cool_matches]
cool_threshold = 1
for number in threshold_nums:
    cool_threshold *= number
print(f"Cool threshold: {cool_threshold}")
print(f"{len(emojis)} emojis found in the text. The cool ones are:")
for emoji in emojis:
    emoji_value = sum([ord(character) for character in emoji if character not in ["*", ":"]])
    if emoji_value >= cool_threshold:
        print(emoji)


################################################   Task Description   ################################################
# Problem 2 - Emoji Detector
# 
# Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
# Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2302#1.
# 
# Your task is to write a program that extracts emojis from a text and find the threshold based on the input.
# You have to get your cool threshold. It is obtained by multiplying all the digits found in the input.  
# The cool threshold could be a huge number, so be mindful.
# An emoji is valid when:
#     • It is surrounded by 2 characters, either "::" or "**"
#     • It is at least 3 characters long (without the surrounding symbols)
#     • It starts with a capital letter
#     • Continues with lowercase letters only
# Examples of valid emojis: ::Joy::, **Banana**, ::Wink::
# Examples of invalid emojis: ::Joy**, ::fox:es:, **Monk3ys**, :Snak::Es::
# You need to count all valid emojis in the text and calculate their coolness. 
# The coolness of the emoji is determined by summing all the ASCII values of all letters in the emoji. 
# Examples: ::Joy:: - 306, **Banana** - 577, ::Wink:: - 409
# You need to print the result of the cool threshold and, after that to take all emojis out of the text, 
# count them and print only the cool ones on the console.
# Input
#     • On the single input, you will receive a piece of string. 
# Output
#     • On the first line of the output, print the obtained Cool threshold in the format:
# "Cool threshold: {coolThresholdSum}"
#     • On the following line, print the count of all emojis found in the text in format:
# "{countOfAllEmojis} emojis found in the text. The cool ones are:
# {cool emoji 1}
# {cool emoji 2}
# …
# {cool emoji N}"
# Constraints
# There will always be at least one digit in the text!
