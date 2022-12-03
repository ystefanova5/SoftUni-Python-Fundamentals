count = int(input())
plants = {}
for num in range(count):
    plant_name, rarity = input().split("<->")
    plants[plant_name] = {"rarity": rarity, "rating": []}
command = input().split(": ")
while command[0] != "Exhibition":
    plant = command[1].split(" - ")[0]
    if plant not in plants:
        print("error")
    else:
        if command[0] == "Rate":
            rating = command[1].split(" - ")[1]
            plants[plant]["rating"].append(rating)
        elif command[0] == "Update":
            new_rarity = command[1].split(" - ")[1]
            plants[plant]["rarity"] = new_rarity
        elif command[0] == "Reset":
            plants[plant]["rating"] = []
    command = input().split(": ")
print(f"Plants for the exhibition:")
for plant, info in plants.items():
    rarity = info["rarity"]
    ratings = [int(x) for x in info["rating"]]
    if len(ratings) > 0:
        average_rating = sum(ratings) / len(ratings)
    else:
        average_rating = 0
    print(f"- {plant}; Rarity: {rarity}; Rating: {average_rating:.2f}")


################################################   Task Description   ################################################
# Problem 3 - Plant Discovery
# 
# Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
# Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2518#2.
# 
# You have now returned from your world tour. On your way, you have discovered some new plants, 
# and you want to gather some information about them and create an exhibition to see which plant is highest rated.
# On the first line, you will receive a number n. 
# On the next n lines, you will be given some information about the plants that you have discovered in the format: 
# "{plant}<->{rarity}". 
# Store that information because you will need it later. If you receive a plant more than once, update its rarity.
# After that, until you receive the command "Exhibition", you will be given some of these commands:
# • "Rate: {plant} - {rating}" – add the given rating to the plant (store all ratings)
# • "Update: {plant} - {new_rarity}" – update the rarity of the plant with the new one
# • "Reset: {plant}" – remove all the ratings of the given plant
# Note: If any given plant name is invalid, print "error"
# After the command "Exhibition", print the information that you have about the plants in the following format:
# "Plants for the exhibition:
# - {plant_name1}; Rarity: {rarity}; Rating: {average_rating}
# - {plant_name2}; Rarity: {rarity}; Rating: {average_rating}
# …
# - {plant_nameN}; Rarity: {rarity}; Rating: {average_rating}"
# The average rating should be formatted to the second decimal place.
# Input / Constraints
# • You will receive the input as described above
# • JavaScript: you will receive a list of strings
# Output
# • Print the information about all plants as described above
