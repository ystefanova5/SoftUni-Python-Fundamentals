strings_list = []
command = input()

while command != "stop":
    strings_list.append(command)
    command = input()

strings_dict = {}
for index, element in enumerate(strings_list):
    if index % 2 == 0:
        if element not in strings_dict:
            strings_dict[element] = int(strings_list[index + 1])
        else:
            strings_dict[element] += int(strings_list[index + 1])

for key, value in strings_dict.items():
    print(f"{key} -> {value}")
    

################################################   Task Description   ################################################
# 2. A Miner Task
# You will be given a sequence of strings, each on a new line until you receive the "stop" command.
# Every odd line on the console represents a resource (e.g., Gold, Silver, Copper, and so on) and every even - quantity.
# Your task is to collect the resources and print them each on a new line.
# Print the resources and their quantities in the following format:
# "{resource} -> {quantity}"
# The quantities will be in the range [1 … 2 000 000 000].
