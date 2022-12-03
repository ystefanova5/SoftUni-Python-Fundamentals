heroes_count = int(input())
party = {}
for num in range(heroes_count):
    hero, hit_points, mana = input().split()
    party[hero] = {"hit points": int(hit_points), "mana": int(mana)}
command = input().split(" - ")
while command[0] != "End":
    hero_name = command[1]
    if command[0] == "CastSpell":
        mana_needed, spell_name = int(command[2]), command[3]
        if party[hero_name]["mana"] >= mana_needed:
            party[hero_name]["mana"] -= mana_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {party[hero_name]['mana']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif command[0] == "TakeDamage":
        damage, attacker = int(command[2]), command[3]
        party[hero_name]["hit points"] -= damage
        if party[hero_name]["hit points"] > 0:
            current_hp = party[hero_name]['hit points']
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {current_hp} HP left!")
        else:
            print(f"{hero_name} has been killed by {attacker}!")
            del party[hero_name]
    elif command[0] == "Recharge":
        recharge_amount = int(command[2])
        current_mana = party[hero_name]["mana"]
        if current_mana + recharge_amount <= 200:
            amount_recovered = recharge_amount
        else:
            amount_recovered = 200 - current_mana
        party[hero_name]["mana"] += amount_recovered
        print(f"{hero_name} recharged for {amount_recovered} MP!")
    elif command[0] == "Heal":
        heal_amount = int(command[2])
        current_hit_points = party[hero_name]["hit points"]
        if current_hit_points + heal_amount <= 100:
            amount_recovered = heal_amount
        else:
            amount_recovered = 100 - current_hit_points
        party[hero_name]["hit points"] += amount_recovered
        print(f"{hero_name} healed for {amount_recovered} HP!")
    command = input().split(" - ")
for hero, info in party.items():
    print(hero)
    print(f"  HP: {party[hero]['hit points']}")
    print(f"  MP: {party[hero]['mana']}")


################################################   Task Description   ################################################
# Problem 3 - Heroes of Code and Logic VII
# 
# Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
# Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2303#0.
# 
# You got your hands on the most recent update on the best MMORPG of all time – Heroes of Code and Logic. 
# You want to play it all day long! So cancel all other arrangements and create your party!
# On the first line of the standard input, you will receive an integer n – the number of heroes that you can 
# choose for your party. On the next n lines, the heroes themselves will follow with their hit points and mana points 
# separated by a single space in the following format: 
# "{hero name} {HP} {MP}"
#     - HP stands for hit points and MP for mana points
#     - a hero can have a maximum of 100 HP and 200 MP
# After you have successfully picked your heroes, you can start playing the game. 
# You will be receiving different commands, each on a new line, separated by " – ", until the "End" command is given. 
# There are several actions that the heroes can perform:
# "CastSpell – {hero name} – {MP needed} – {spell name}"
#     • If the hero has the required MP, he casts the spell, thus reducing his MP. Print this message: 
#         o "{hero name} has successfully cast {spell name} and now has {mana points left} MP!"
#     • If the hero is unable to cast the spell print:
#         o "{hero name} does not have enough MP to cast {spell name}!"
#           "TakeDamage – {hero name} – {damage} – {attacker}"
#     • Reduce the hero HP by the given damage amount. If the hero is still alive (his HP is greater than 0) print:
#         o "{hero name} was hit for {damage} HP by {attacker} and now has {current HP} HP left!"
#     • If the hero has died, remove him from your party and print:
#         o "{hero name} has been killed by {attacker}!"
#           "Recharge – {hero name} – {amount}"
#     • The hero increases his MP. If it brings the MP of the hero above the maximum value (200), 
#       MP is increased to 200. (the MP can't go over the maximum value).
#     • Print the following message:
#         o "{hero name} recharged for {amount recovered} MP!"
#           "Heal – {hero name} – {amount}"
#     • The hero increases his HP. If a command is given that would bring the HP of the hero above 
#       the maximum value (100), HP is increased to 100 (the HP can't go over the maximum value).
#     • Print the following message:
#         o "{hero name} healed for {amount recovered} HP!"
# Input
#     • On the first line of the standard input, you will receive an integer n
#     • On the following n lines, the heroes themselves will follow with their hit points and mana points 
#       separated by a space in the following format:
#       "{hero name} {HP} {MP}"
#     • You will be receiving different commands, each on a new line, separated by " – ", 
#       until the "End" command is given
# Output
#     • Print all members of your party who are still alive, 
#       in the following format (their HP/MP need to be indented 2 spaces):
#       "{hero name}
#         HP: {current HP}
#         MP: {current MP}"
# Constraints
#     • The starting HP/MP of the heroes will be valid, 32-bit integers will never be negative 
#       or exceed the respective limits.
#     • The HP/MP amounts in the commands will never be negative.
#     • The hero names in the commands will always be valid members of your party. No need to check that explicitly.
