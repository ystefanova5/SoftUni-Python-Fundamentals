key = int(input())
number_of_lines = int(input())
for _ in range(number_of_lines):
    input_letter = input()
    output_letter = chr(ord(input_letter) + key)
    print(output_letter, end="")


################################################   Task Description   ################################################
# 3. Decrypting Messages
# On the first line, you will receive a key (integer).
# On the second line, you will receive n – the number of lines, which will follow. 
# On the next n lines – you will receive a lower and an uppercase letter per line.
# You should add the key to each of the characters and append them to a message. 
# In the end, print the decrypted message. 
