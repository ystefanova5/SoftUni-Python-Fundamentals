message = input()
while True:
    command = input()
    if command == "Reveal":
        break
    operation = command.split(":|:")[0]
    if operation == "InsertSpace":
        index = int(command.split(":|:")[1])
        message = message[:index] + " " + message[index:]
    elif operation == "Reverse":
        substring = command.split(":|:")[1]
        if substring in message:
            message = message.replace(substring, "", 1)
            message += substring[::-1]
        else:
            print("error")
            continue
    elif operation == "ChangeAll":
        substring, replacement = command.split(":|:")[1], command.split(":|:")[2]
        message = message.replace(substring, replacement)
    print(message)

print(f"You have a new text message: {message}")


################################################   Task Description   ################################################
# Problem 1 - Secret Chat
# 
# Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
# Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2307#0.
# 
# You have plenty of free time, so you decide to write a program that conceals and reveals your received messages. 
# Go ahead and type it in!
# On the first line of the input, you will receive the concealed message. 
# After that, until the "Reveal" command is given, you will receive strings with instructions for different  
# operations that need to be performed upon the concealed message to interpret it and reveal its actual content. 
# There are several types of instructions, split by ":|:"
# • "InsertSpace:|:{index}":
#     o Inserts a single space at the given index. The given index will always be valid.
# • "Reverse:|:{substring}":
#     o If the message contains the given substring, cut it out, reverse it and add it at the end of the message. 
#     o If not, print "error".
#     o This operation should replace only the first occurrence of the given substring 
#       if there are two or more occurrences.
# • "ChangeAll:|:{substring}:|:{replacement}":
#     o Changes all occurrences of the given substring with the replacement text.
# Input / Constraints
# • On the first line, you will receive a string with a message.
# • On the following lines, you will be receiving commands, split by ":|:".
# Output
# • After each set of instructions, print the resulting string. 
# • After the "Reveal" command is received, print this message:
# "You have a new text message: {message}"
