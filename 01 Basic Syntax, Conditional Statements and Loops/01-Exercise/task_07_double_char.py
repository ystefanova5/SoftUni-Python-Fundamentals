command = input()
while command != "End":
    current_string = command
    double_char_string = ""
    if current_string != "SoftUni":
        for i in range(len(current_string)):
            double_char_string += current_string[i] * 2
        print(double_char_string)
    command = input()


################################################   Task Description   ################################################
# 7. Double Char
# You will be given strings until you receive the command "End". 
# For each string given, you should print a string in which each character (case-sensitive) is repeated twice. 
# Note that if you receive the string "SoftUni", you should NOT print it!
