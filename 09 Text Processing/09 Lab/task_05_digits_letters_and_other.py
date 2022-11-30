user_input = input()
digits = ""
letters = ""
other_characters = ""
for symbol in user_input:
    if symbol.isdigit():
        digits += symbol
    elif symbol.isalpha():
        letters += symbol
    else:
        other_characters += symbol
print(digits)
print(letters)
print(other_characters)


################################################## Task Description ##################################################
# 5. Digits, Letters, and Other
# Write a program that receives a single string.
# On the first line, print all the digits found in the string, on the second – all the letters,
# and on the third – all the other characters.
# There will always be at least one digit, one letter, and one other character.
