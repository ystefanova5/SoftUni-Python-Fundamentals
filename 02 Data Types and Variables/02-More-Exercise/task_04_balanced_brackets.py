number_of_lines = int(input())
open_bracket = False
closed_bracket = False
parentheses_are_balanced = False
for _ in range(number_of_lines):
    symbol = input()
    if symbol == "(":
        if not open_bracket:
            open_bracket = True
        else:
            parentheses_are_balanced = False
            break
    elif symbol == ")":
        if not open_bracket:
            parentheses_are_balanced = False
            break
        elif not closed_bracket:
            closed_bracket = True
            if open_bracket and closed_bracket:
                closed_bracket = False
                open_bracket = False
                parentheses_are_balanced = True
            else:
                parentheses_are_balanced = False
        else:
            parentheses_are_balanced = False
            break
if parentheses_are_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")


################################################   Task Description   ################################################
# 4. Balanced Brackets
# On the first line, you will receive n – the number of lines, which will follow. 
# On the following n lines, you will receive one of the following:
#     • Opening bracket – "(",
#     • Closing bracket – ")" or
#     • Random string
# Your task is to find out if the brackets are balanced. 
# That means after every closing bracket should follow an opening one. 
# Nested parentheses are not valid, and if, for example, two consecutive opening brackets exist, 
# the expression should be marked as unbalanced. 
# You should print "BALANCED" if the parentheses are balanced and "UNBALANCED" otherwise.
