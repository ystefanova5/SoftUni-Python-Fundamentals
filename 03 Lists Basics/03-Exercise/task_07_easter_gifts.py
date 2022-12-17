gifts_string = input()
gifts_list = gifts_string.split(" ")
command = input()
while command != "No Money":
    command_list = command.split(" ")
    command = command_list[0]
    gift = command_list[1]
    index = command_list[-1]
    if (gift != index) and (0 <= int(index) < len(gifts_list)):
        index_is_valid = True
    else:
        index_is_valid = False
    if command == "OutOfStock":
        for i in range(len(gifts_list)):
            if gifts_list[i] == gift:
                gifts_list[i] = "None"
    elif command == "Required":
        if index_is_valid:
            gifts_list[int(index)] = gift
    elif command == "JustInCase":
        gifts_list[-1] = gift
    command = input()
for g in range(len(gifts_list)):
    if gifts_list[g] != "None":
        print(gifts_list[g], end=" ")


################################################   Task Description   ################################################
# 7. * Easter Gifts
# As a good friend, you decide to buy presents for your friends.
# Create a program that helps you plan the gifts for your friends and family. 
# First, you are going to receive the gifts you plan on buying on a single line, 
# separated by space, in the following format:
# "{gift1} {gift2} {gift3}… {giftn}"
# Then you will start receiving commands until you read the "No Money" message. There are three possible commands:
#     • "OutOfStock {gift}"
#         o Find the gifts with this name in your collection, if any, and change their values to "None".  
#     • "Required {gift} {index}"
#         o If the index is valid, replace the gift on the given index with the given gift. 
#     • "JustInCase {gift}"
#         o Replace the value of your last gift with this one. 
# In the end, print the gifts on a single line, except the ones with value "None", 
# separated by a single space in the following format:
# "{gift1} {gift2} {gift3} … {giftn}"
# Input / Constraints
#     • On the 1st line,  you will receive the names of the gifts, separated by a single space.
#     • On the following lines, until the "No Money" command is received, you will be receiving commands.
#     • The input will always be valid.
# Output
#     • Print the gifts in the format described above.
