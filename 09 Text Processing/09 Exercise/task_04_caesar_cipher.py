user_input = input()
encrypted_message = ""
for symbol in user_input:
    encrypted_message += chr(ord(symbol) + 3)
print(encrypted_message)


################################################   Task Description   ################################################
# 4. Caesar Cipher
# Write a program that returns an encrypted version of the same text. 
# Encrypt the text by replacing each character with the corresponding character 
# three positions forward in the ASCII table. For example, A would be replaced with D, B would become E, and so on. 
# Print the encrypted text.
