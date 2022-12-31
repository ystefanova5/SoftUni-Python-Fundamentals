def data_types_operations(data_type, user_input):
    if data_type == "int":
        return int(user_input) * 2
    elif data_type == "real":
        return f"{float(user_input) * 1.5:.2f}"
    else:
        return f"${user_input}$"


current_data_type = input()
current_user_input = input()
print(data_types_operations(current_data_type, current_user_input))


################################################   Task Description   ################################################
# 1. Data Types
# Write a function that, depending on the first line of the input, 
# reads one of the following strings: "int", "real", or "string".
#     • If the data type is an int, multiply the number by 2.
#     • If the data type is real, multiply the number by 1.5 and format the result to the second decimal point.
#     • If the data type is a string, surround the input with "$".
# Print the result on the console.
