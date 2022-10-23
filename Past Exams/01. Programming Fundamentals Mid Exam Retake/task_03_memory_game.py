def cheat_check(list_name, index1, index2, num_moves):
    cheat_detected = False
    message = None
    if index1 == index2:
        cheat_detected = True
    if index1 not in range(len(list_name)) or index2 not in range(len(list_name)):
        cheat_detected = True
    if cheat_detected:
        message = "Invalid input! Adding additional elements to the board"
        new_symbol = f"-{num_moves}a"
        index_to_insert = int(len(list_name) / 2)
        list_name.insert(index_to_insert, new_symbol)
        next_index = list_name.index(new_symbol)
        list_name.insert(next_index, new_symbol)
    return message, list_name


def check_matching_elements(list_name, index1, index2):
    message = ""
    we_have_matching_elements = False
    symbol = list_name[index1]
    if list_name[index1] == list_name[index2]:
        we_have_matching_elements = True
    if we_have_matching_elements:
        message = f"Congrats! You have found matching elements - {symbol}!"
        list_name.remove(symbol)
        list_name.remove(symbol)
    else:
        message = "Try again!"
    return message, list_name


elements = input().split()
command = input()
moves = 0
while command != "end":
    first_index = int(command.split()[0])
    second_index = int(command.split()[1])
    moves += 1
    text, elements = cheat_check(elements, first_index, second_index, moves)
    if text is not None:
        print("Invalid input! Adding additional elements to the board")
    else:
        result_message, elements = check_matching_elements(elements, first_index, second_index)
        print(result_message)
    if len(elements) == 0:
        print(f"You have won in {moves} turns!")
        break
    command = input()
if len(elements) > 0:
    print("Sorry you lose :(")
    print(" ".join(elements))
