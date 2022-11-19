import re

number_of_messages = int(input())
attacked_planets = []
destroyed_planets = []
for message in range(number_of_messages):
    current_message = input()
    encryption_pattern = r"[SsTtAaRr]"
    decryption_key = len(re.findall(encryption_pattern, current_message))
    decrypted_message = ""
    for symbol in current_message:
        decrypted_message += chr(ord(symbol) - decryption_key)
    validation_pattern = r"@[A-Za-z]+[^@\-\!\:\>]*\:\d+[^@\-\!\:\>]*\![AD]\![^@\-\!\:\>]*\-\>\d+"
    validation = re.findall(validation_pattern, decrypted_message)
    if validation:
        name_pattern = r"@[A-Za-z]+"
        population_pattern = r"\:\d+"
        attack_pattern = r"\![AD]\!"
        soldier_pattern = r"\-\>\d+"
        planet_name = re.findall(name_pattern, decrypted_message)[0][1:]
        attack_type = re.findall(attack_pattern, decrypted_message)[0][1]
        if attack_type == "A":
            attacked_planets.append(planet_name)
        elif attack_type == "D":
            destroyed_planets.append(planet_name)
print(f"Attacked planets: {len(attacked_planets)}")
if len(attacked_planets) > 0:
    for planet in sorted(attacked_planets):
        print(f"-> {planet}")
print(f"Destroyed planets: {len(destroyed_planets)}")
if len(destroyed_planets) > 0:
    for planet in sorted(destroyed_planets):
        print(f"-> {planet}")


################################################   Task Description   ################################################
# 3. Star Enigma
# The war is in its peak, but you, young Padawan, can turn the tides with your programming skills.
# You are tasked to create a program to decrypt the messages of The Order and prevent the death of hundreds of lives.
# You will receive several messages, which are encrypted using the legendary star enigma.
# You should decrypt the messages, following these rules:
# To properly decrypt a message, you should count all the letters [s, t, a, r] – case insensitive
# and remove the count from the current ASCII value of each symbol of the encrypted message.
# After decryption:
# Each message should have a planet name, population,
# attack type ('A', as attack or 'D', as destruction) and soldier count.
# The planet name starts after '@' and contains only letters from the Latin alphabet.
# The planet population starts after ':' and is an Integer;
# The attack type may be "A"(attack) or "D"(destruction) and must be surrounded by "!" (exclamation mark).
# The soldier count starts after "->" and should be an Integer.
# The order in the message should be: planet name -> planet population -> attack type -> soldier count.
# Each part can be separated from the others by any character except: '@', '-', '!', ':' and '>'.
# Input / Constraints
# • The first line holds n – the number of messages– integer in range [1…100];
# • On the next n lines, you will be receiving encrypted messages.
# Output
# After decrypting all messages, you should print the decrypted information in the following format:
# First print the attacked planets, then the destroyed planets.
# "Attacked planets: {attackedPlanetsCount}"
# "-> {planetName}"
# "Destroyed planets: {destroyedPlanetsCount}"
# "-> {planetName}"
# The planets should be ordered by name alphabetically.
