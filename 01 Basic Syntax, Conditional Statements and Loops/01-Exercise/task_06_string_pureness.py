number_of_strings = int(input())
for _ in range(number_of_strings):
    current_string = input()
    for i in range(len(current_string)):
        if current_string[i] == "," or current_string[i] == "." or current_string[i] == "_":
            print(f"{current_string} is not pure!")
            break
    else:
        print(f"{current_string} is pure.")