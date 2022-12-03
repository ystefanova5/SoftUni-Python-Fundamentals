number_of_pieces = int(input())
music_collection = {}
for piece in range(number_of_pieces):
    current_piece, current_composer, current_key = input().split("|")
    music_collection[current_piece] = {"composer": current_composer, "key": current_key}
command = input()
while command != "Stop":
    current_command = command.split("|")[0]
    if current_command == "Add":
        piece, composer, key = command.split("|")[1], command.split("|")[2], command.split("|")[3]
        if piece not in music_collection:
            music_collection[piece] = {"composer": composer, "key": key}
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    elif current_command == "Remove":
        piece = command.split("|")[1]
        if piece in music_collection:
            del music_collection[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif current_command == "ChangeKey":
        piece, new_key = command.split("|")[1], command.split("|")[2]
        if piece in music_collection:
            music_collection[piece]["key"] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    command = input()
for key, value in music_collection.items():
    print(f"{key} -> Composer: {value['composer']}, Key: {value['key']}")


################################################   Task Description   ################################################
# Problem 3 - The Pianist
# 
# Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
# Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2525#2.
# 
# You are a pianist, and you like to keep a list of your favorite piano pieces. 
# Create a program to help you organize it and add, change, remove pieces from it!
# On the first line of the standard input, you will receive an integer n – the number of pieces you will initially have. 
# On the next n lines, the pieces themselves will follow with their composer and key, 
# separated by "|" in the following format: "{piece}|{composer}|{key}".
# Then, you will be receiving different commands, each on a new line, separated by "|", until the "Stop" command is given:
# • "Add|{piece}|{composer}|{key}":
#   o You need to add the given piece with the information about it to the other pieces and print:
#   "{piece} by {composer} in {key} added to the collection!"
#   o If the piece is already in the collection, print:
#   "{piece} is already in the collection!"
# • "Remove|{piece}":
#   o If the piece is in the collection, remove it and print:
#   "Successfully removed {piece}!"
#   o Otherwise, print:
#   "Invalid operation! {piece} does not exist in the collection."
# • "ChangeKey|{piece}|{new key}":
#   o If the piece is in the collection, change its key with the given one and print:
#   "Changed the key of {piece} to {new key}!"
#   o Otherwise, print:
#   "Invalid operation! {piece} does not exist in the collection."
# Upon receiving the "Stop" command, you need to print all pieces in your collection in the following format:
# "{Piece} -> Composer: {composer}, Key: {key}"
# Input/Constraints
# • You will receive a single integer at first – the initial number of pieces in the collection
# • For each piece, you will receive a single line of text with information about it.
# • Then you will receive multiple commands in the way described above until the command "Stop".
# Output
# • All the output messages with the appropriate formats are described in the problem description.
