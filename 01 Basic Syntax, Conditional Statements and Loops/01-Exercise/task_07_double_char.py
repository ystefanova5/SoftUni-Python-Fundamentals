command = input()
while command != "End":
    current_string = command
    double_char_string = ""
    if current_string != "SoftUni":
        for i in range(len(current_string)):
            double_char_string += current_string[i] * 2
        print(double_char_string)
    command = input()