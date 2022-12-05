spell = input()
command = input().split()
while command[0] != "Abracadabra":
    current_command = command[0]
    
    if current_command == "Abjuration":
        spell = spell.upper()
        print(spell)
        
    elif current_command == "Necromancy":
        spell = spell.lower()
        print(spell)
        
    elif current_command == "Illusion":
        index, letter = int(command[1]), command[2]
        if 0 <= index < len(spell):
            spell = spell[:index] + letter + spell[index + 1:]
            print("Done!")
        else:
            print("The spell was too weak.")
            
    elif current_command == "Divination":
        first_substring, second_substring = command[1], command[2]
        if first_substring in spell:
            spell = spell.replace(first_substring, second_substring)
            print(spell)
            
    elif current_command == "Alteration":
        substring = command[1]
        if substring in spell:
            spell = spell.replace(substring, "")
            print(spell)
            
    else:
        print("The spell did not work!")
    command = input().split()


################################################   Task Description   ################################################
# 1. Hogwarts
