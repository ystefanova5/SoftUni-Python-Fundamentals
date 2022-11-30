key_sequence = [int(x) for x in input().split()]
command = input()
while command != "find":
    message = ""
    current_string = [ord(x) for x in command]
    if len(command) > len(key_sequence):
        repetitions = len(command) // len(key_sequence)
        new_key_sequence = key_sequence * repetitions
        diff = len(command) - len(new_key_sequence)
        if diff > 0:
            new_key_sequence += key_sequence[:diff]
    else:
        new_key_sequence = key_sequence
    for index, symbol in enumerate(command):
        message += chr(ord(symbol) - int(new_key_sequence[index]))
    treasure_type = message.split("&")[1]
    coordinates_start_index = message.index("<") + 1
    coordinates_end_index = message.index(">")
    coordinates = message[coordinates_start_index:coordinates_end_index]
    print(f"Found {treasure_type} at {coordinates}")
    command = input()


################################################   Task Description   ################################################
# 3. Treasure Finder
# Write a program that decrypts a message by a given key and gathers information
# about hidden treasure type and its coordinates.
# On the first line, you will receive a key (sequence of numbers separated by a space).
# On the next few lines, you will receive lines with strings until you get the command "find".
# You should loop through every string and decrease the ASCII code of each character
# with a corresponding number of the key sequence. You choose a key number from the sequence by just looping through it.
# If the length of the key sequence is less than the string sequence, you should continue looping from the beginning.
# For more clarification, see the example below.
# After decrypting the message, you will get a type of treasure and its coordinates.
# The type will be between the symbol "&", and the coordinates - between the symbols "<' and '>'.
# For each line print the type and the coordinates in the format "Found {type} at {coordinates}".
