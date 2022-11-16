phonebook = {}
command = input().split("-")
while len(command) > 1:
    current_key = command[0]
    current_value = command[1]
    phonebook[current_key] = current_value
    command = input().split("-")

searched_numbers = int(command[0])
for number in range(searched_numbers):
    searched_name = input()
    if searched_name in phonebook:
        print(f"{searched_name} -> {phonebook[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")


################################################   Task Description   ################################################
# 4. Phonebook
# Write a program that receives info from the console about people and their phone numbers.
# Each entry should have a name and a number (both strings) separated by a "-".
# If you receive a name that already exists in the phonebook, update its number.
# After filling the phonebook, you will receive a number – N.
# Your program should be able to perform a search of contact by name and print its details in the format:
# "{name} -> {number}".
# In case the contact isn't found, print: "Contact {name} does not exist."
