encrypted_message = input()
command = input()
while command != "Decode":
    current_operation = command.split("|")[0]
    if current_operation == "Move":
        number_of_letters = int(command.split("|")[1])
        encrypted_message = encrypted_message[number_of_letters:] + encrypted_message[0:number_of_letters]
    elif current_operation == "Insert":
        index, value = int(command.split("|")[1]), command.split("|")[2]
        if index != 0:
            encrypted_message = encrypted_message[0:index] + value + encrypted_message[index:]
        else:
            encrypted_message = value + encrypted_message
    elif current_operation == "ChangeAll":
        substring, replacement = command.split("|")[1], command.split("|")[2]
        encrypted_message = encrypted_message.replace(substring, replacement)
    command = input()
print(f"The decrypted message is: {encrypted_message}")


################################################   Task Description   ################################################
# Problem 1 - The Imitation Game
# 
# Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
# Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2525#0.
# 
# During World War 2, you are a mathematician who has joined the cryptography team to decipher the enemy's enigma code. 
# Your job is to create a program to crack the codes. 
# On the first line of the input, you will receive the encrypted message. 
# After that, until the "Decode" command is given, you will be receiving strings with instructions 
# for different operations that need to be performed upon the concealed message to interpret it and reveal its true content. 
# There are several types of instructions, split by '|'
# • "Move {number of letters}":
#   o Moves the first n letters to the back of the string
# • "Insert {index} {value}":
#   o Inserts the given value before the given index in the string
# • "ChangeAll {substring} {replacement}":
#   o Changes all occurrences of the given substring with the replacement text
# Input / Constraints
# • On the first line, you will receive a string with a message.
# • On the following lines, you will be receiving commands, split by '|' .
# Output
# • After the "Decode" command is received, print this message:
# "The decrypted message is: {message}"
