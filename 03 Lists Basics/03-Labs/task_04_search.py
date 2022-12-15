number = int(input())
word = input()
full_list = []
filtered_list = []
for _ in range(number):
    input_string = input()
    full_list.append(input_string)
    if word in input_string:
        filtered_list.append(input_string)
print(full_list)
print(filtered_list)


################################################   Task Description   ################################################
# 4. Search
# On the first line, you will receive a number n. On the second line, you will receive a word. 
# On the following n lines, you will be given some strings. You should add them to a list and print them. 
# After that, you should filter out only the strings that include the given word and print that list too.
