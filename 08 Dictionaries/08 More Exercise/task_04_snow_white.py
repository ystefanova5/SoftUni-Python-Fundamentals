dwarfs = {}
input_line = input()
while input_line != "Once upon a time":
    dwarf_info = input_line.split(" <:> ")
    dwarf_name, dwarf_hat_color, dwarf_physics = dwarf_info[0], dwarf_info[1], int(dwarf_info[2])
    if dwarf_hat_color not in dwarfs:
        dwarfs[dwarf_hat_color] = {}
    else:
        if dwarf_name not in dwarfs[dwarf_hat_color]:
            dwarfs[dwarf_hat_color][dwarf_name] = 0
        else:
            if dwarf_physics < dwarfs[dwarf_hat_color][dwarf_name]:
                dwarf_physics = dwarfs[dwarf_hat_color][dwarf_name]
    dwarfs[dwarf_hat_color][dwarf_name] = dwarf_physics
    input_line = input()

dwarfs_dict = {}
for hat_color, members in dwarfs.items():
    hat_length = len(members)
    for dwarf, physics in members.items():
        dwarf_name_color = f"{dwarf}|{hat_color}"
        dwarfs_dict[dwarf_name_color] = {"name": dwarf, "physics": physics, "members": hat_length,
                                         "hat_color": hat_color}

for item in sorted(dwarfs_dict, key=lambda k: (dwarfs_dict[k]['physics'], dwarfs_dict[k]['members']), reverse=True):
    current_dwarf = dwarfs_dict[item]
    print(f"({current_dwarf['hat_color']}) {current_dwarf['name']} <-> {current_dwarf['physics']}")


################################ Task Description ################################
# 4. Snow White
# Snow White loves her dwarfs, but there are so many, and she doesn't know how to order them. 
# Does she order them by name? Or by color of their hat? Or by physics? 
# She can't decide, so it's up to you to write a program that does it for her.
# You will be receiving several input lines which contain data about each dwarf in the following format:
# {dwarf_name} <:> {dwarf_hat_color} <:> {dwarf_physics}
# The "dwarf_name" and the "dwarf_hat_color" are strings. The "dwarf_physics" is an integer.
# You must store the data about the dwarfs in your program. There are several rules though:
# • If 2 dwarfs have the same name but different color, they should be considered different dwarfs, 
#   and you should store them both.
# • If 2 dwarfs have the same name and the same color, store the one with the higher physics.
# When you receive the command "Once upon a time", the input ends. 
# You must order the dwarfs by physics in descending order 
# and then by total count of dwarfs with the same hat color in descending order. 
# Then you must print them all.
# Input
# • The input will consist of several input lines, containing dwarf data in the format, specified above.
# • The input ends when you receive the command "Once upon a time". 
# Output
# • As output, you must print the dwarfs, ordered in the way, specified above.
# • The output format is: "({hat_color}) {name} <-> {physics}"
# Constraints
# • The "dwarf_name" will be a string which may contain any ASCII character except ' ' (space), '<', ':', '>'.
# • The "dwarf_hat_color" will be a string which may contain any ASCII character except ' ' (space), '<', ':', '>'.
# • The "dwarf_physics" will be an integer in range [0, 231 – 1].
# • There will be no invalid input lines.
# • If all sorting criteria fail, the order should be by order of input.
# • Allowed working time / memory: 100ms / 16MB.
