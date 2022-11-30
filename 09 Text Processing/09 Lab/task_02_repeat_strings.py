strings_sequence = input().split()
result_string = ""
for string in strings_sequence:
    result_string += string * len(string)
print(result_string)


###################################### Task Description ######################################
# 2. Repeat Strings
# Write a program that reads a sequence of strings, separated by a single space. 
# Each string should be repeated N times, where N is the length of the string. 
# Print the final strings concatenated into one string.
