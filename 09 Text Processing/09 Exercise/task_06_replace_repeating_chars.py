text = input()
for letter in text:
    double_letter = letter + letter
    text = text.replace(double_letter, letter)
print(text)


################################################   Task Description   ################################################
# 6. Replace Repeating Chars
# Write a program that reads a string from the console
# and replaces any sequence of the same letters with a single corresponding letter.
