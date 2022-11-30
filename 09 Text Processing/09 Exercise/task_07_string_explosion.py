text = input()
result_text = ""
explosion_strength = 0
for index, symbol in enumerate(text):
    if symbol != ">" and explosion_strength == 0:
        result_text += symbol
    elif symbol == ">":
        result_text += symbol
        explosion_strength += int(text[index + 1])
    elif symbol != ">" and explosion_strength > 0:
        explosion_strength -= 1
print(result_text)


################################################   Task Description   ################################################
# 7. String Explosion
# Write a program that reads a string from the console that contains:
# · Explosions marked with '>'
# · Immediately after the mark, there will be an integer x, which signifies the strength of the explosion
# · Any other characters
# Your task is to delete x characters, starting after the exploded character ('>').
# If you find another explosion mark ('>') while deleting characters,
# you should add the strength to your previous explosion. You should not delete the explosion character – '>'.
# When all characters are processed, print the final string.
# Constraints
# · You will always receive strength for the explosions
# · The path will consist only of letters from the Latin alphabet, integers, and the char '>'
# · The strength of the punches will be in the interval [0…9]
