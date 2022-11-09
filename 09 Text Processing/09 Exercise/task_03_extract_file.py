path = input().split("\\")
last_element = path[-1].split(".")
file_name = last_element[0]
file_extension = last_element[1]
print(f"File name: {file_name}")
print(f"File extension: {file_extension}")


################################################   Task Description   ################################################
# 3. Extract File
# Write a program that reads the path to a file and subtracts the file name and its extension.
