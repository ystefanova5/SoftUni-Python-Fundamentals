import re

text = input()
word = input()
pattern = fr"\b({word.lower()})\b"
matches = re.findall(pattern, text.lower())
print(len(matches))


################################################   Task Description   ################################################
# 3. Find Occurrences of Word in Sentence
# Write a program that finds how many times a word is used in a string. 
# The output is a single number indicating the number of times the string contains the word. 
# Note that letter case does not matter – it is case-insensitive.
