targeted_cities = {}

first_command = input().split("||")
while first_command[0] != "Sail":
    town_name, population, gold = first_command[0], int(first_command[1]), int(first_command[2])
    if town_name not in targeted_cities:
        targeted_cities[town_name] = {"population": population, "gold": gold}
    else:
        targeted_cities[town_name]["population"] += population
        targeted_cities[town_name]["gold"] += gold
    first_command = input().split("||")

second_command = input().split("=>")
while second_command[0] != "End":
    action, town = second_command[0], second_command[1]
    if action == "Plunder":
        people, plundered_gold = int(second_command[2]), int(second_command[3])
        targeted_cities[town]["population"] -= people
        targeted_cities[town]["gold"] -= plundered_gold
        print(f"{town} plundered! {plundered_gold} gold stolen, {people} citizens killed.")
        if targeted_cities[town]["population"] == 0 or targeted_cities[town]["gold"] == 0:
            print(f"{town} has been wiped off the map!")
            del targeted_cities[town]
    elif action == "Prosper":
        added_gold = int(second_command[2])
        if added_gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            targeted_cities[town]["gold"] += added_gold
            total_gold = targeted_cities[town]["gold"]
            print(f"{added_gold} gold added to the city treasury. {town} now has {total_gold} gold.")
    second_command = input().split("=>")

if targeted_cities:
    print(f"Ahoy, Captain! There are {len(targeted_cities)} wealthy settlements to go to:")
    for key, value in targeted_cities.items():
        print(f"{key} -> Population: {value['population']} citizens, Gold: {value['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")


################################################   Task Description   ################################################
# Problem 3 - P!rates
# 
# Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
# Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2302#2.
# 
Anno 1681. The Caribbean. The golden age of piracy. You are a well-known pirate captain by the name of Jack Daniels. 
Together with your comrades Jim (Beam) and Johnny (Walker), you have been roaming the seas, 
looking for gold and treasure… and the occasional killing, of course. 
Go ahead, target some wealthy settlements and show them the pirate's way!
Until the "Sail" command is given, you will be receiving:
    • You and your crew have targeted cities, with their population and gold, separated by "||".
    • If you receive a city that has already been received, you have to increase 
      the population and gold with the given values.
After the "Sail" command, you will start receiving lines of text representing events until the "End" command is given. 
Events will be in the following format:
    • "Plunder=>{town}=>{people}=>{gold}"
        o You have successfully attacked and plundered the town, killing the given number of people 
          and stealing the respective amount of gold. 
        o For every town you attack print this message: "{town} plundered! {gold} gold stolen, {people} citizens killed."
        o If any of those two values (population or gold) reaches zero, the town is disbanded.
             You need to remove it from your collection of targeted cities and print the following message: 
              "{town} has been wiped off the map!"
        o There will be no case of receiving more people or gold than there is in the city.
    • "Prosper=>{town}=>{gold}"
        o There has been dramatic economic growth in the given city, increasing its treasury by the given amount of gold.
        o The gold amount can be a negative number, so be careful. If a negative amount of gold is given, print: 
          "Gold added cannot be a negative number!" and ignore the command.
        o If the given gold is a valid amount, increase the town's gold reserves by the respective amount 
          and print the following message: 
          "{gold added} gold added to the city treasury. {town} now has {total gold} gold."
Input
    • On the first lines, until the "Sail" command, you will be receiving strings representing 
      the cities with their gold and population, separated by "||"
    • On the following lines, until the "End" command, you will be receiving strings representing 
      the actions described above, separated by "=>"
Output
    • After receiving the "End" command, if there are any existing settlements on your list of targets, 
    you need to print all of them, in the following format:
      "Ahoy, Captain! There are {count} wealthy settlements to go to:
      {town1} -> Population: {people} citizens, Gold: {gold} kg
      {town2} -> Population: {people} citizens, Gold: {gold} kg
       …
      {town…n} -> Population: {people} citizens, Gold: {gold} kg"
    • If there are no settlements left to plunder, print:
      "Ahoy, Captain! All targets have been plundered and destroyed!"
Constraints
    • The initial population and gold of the settlements will be valid 32-bit integers, 
      never negative, or exceed the respective limits.
    • The town names in the events will always be valid towns that should be on your list.
