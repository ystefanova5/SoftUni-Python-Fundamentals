banned_words = input().split(", ")
text = input()
for word in banned_words:
    replacement = "*" * len(word)
    text = text.replace(word, replacement)
print(text)


###################################### Task Description ######################################
# 4. Text Filter
# Write a program that receives a text and a string of banned words, separated by a comma and space ", ".
# All banned words in the text should be replaced with the number of asterisks "*", equal to the word's length.
# The ban list will be entered on the first input line and the text - on the second input line.
