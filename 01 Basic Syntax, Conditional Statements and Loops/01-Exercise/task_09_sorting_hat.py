command = input()
hats_are_sorted = True
while command != "Welcome!":
    current_name = command
    current_house = ""
    if current_name == "Voldemort":
        hats_are_sorted = False
        print("You must not speak of that name!")
        break
    else:
        if len(current_name) < 5:
            print(f"{current_name} goes to Gryffindor.")
        elif len(current_name) == 5:
            print(f"{current_name} goes to Slytherin.")
        elif len(current_name) == 6:
            print(f"{current_name} goes to Ravenclaw.")
        else:
            print(f"{current_name} goes to Hufflepuff.")
    command = input()
if hats_are_sorted:
    print("Welcome to Hogwarts.")