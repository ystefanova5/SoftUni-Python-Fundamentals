word = input()
while word != "end":
    reversed_word = word[::-1]
    print(f"{word} = {reversed_word}")
    word = input()

###################################### Task Description ######################################
# 1. Reverse Strings
# You will be given strings on separate lines until you receive an "end" command. 
# Write a program that reverses strings and prints each pair on a separate line in the format "{word} = {reversed_word}".
