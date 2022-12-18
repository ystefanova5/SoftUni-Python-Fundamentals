numbers_sequence = input()
input_string = input()
numbers_list = numbers_sequence.split(" ")
indices_list = []
final_message = ""
for index in range(len(numbers_list)):
    current_combination = numbers_list[index]
    current_sum = 0
    for sequence in range(len(current_combination)):
        current_sum += int(current_combination[sequence])
    indices_list.append(current_sum)
message_indices_count = len(input_string)
for symbol in range(len(numbers_list)):
    current_index = indices_list[symbol]
    while current_index > (message_indices_count - 1):
        current_index -= message_indices_count
    current_symbol = input_string[current_index]
    input_string = input_string[:current_index] + \
                   input_string[current_index + 1::]
    final_message += current_symbol
print(final_message)


################################################   Task Description   ################################################
# 2. Messaging
# On the first line, you will receive a sequence of numbers separated by a single space. 
# On the second line, you will receive a string.
# Your task is to write a program that sends a message only using chars from the given string. 
# Each char the program adds to the message should be found by its index. 
# The index you are looking for is the sum of a number's digits from the first sequence. 
# If the index is greater than the length of the text, 
# continue counting from the beginning (so that you always have a valid index). 
# When you find a char, you should add it to the message and remove it from the string. 
# It means that for the following index, the text will contain one character less.
# Print the final message.
