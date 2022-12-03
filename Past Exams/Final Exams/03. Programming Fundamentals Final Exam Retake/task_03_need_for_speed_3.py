number_of_cars = int(input())
cars = {}
for item in range(number_of_cars):
    car, mileage, fuel = input().split("|")
    cars[car] = {"mileage": int(mileage), "fuel": int(fuel)}
# {'Audi A6': {'mileage': 38000, 'fuel': 62}, 'Mercedes CLS': {'mileage': 11000, 'fuel': 35}, 'Volkswagen Passat CC': {'mileage': 45678, 'fuel': 5}}
command = input()
while command != "Stop":
    action = command.split(" : ")[0]
    if action == "Drive":
        car, distance, fuel = command.split(" : ")[1], int(command.split(" : ")[2]), int(command.split(" : ")[3])
        if cars[car]["fuel"] < fuel:
            print("Not enough fuel to make that ride")
        else:
            cars[car]["fuel"] -= fuel
            cars[car]["mileage"] += distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if cars[car]["mileage"] >= 100000:
                print(f"Time to sell the {car}!")
                del cars[car]
    elif action == "Refuel":
        car, fuel = command.split(" : ")[1], int(command.split(" : ")[2])
        needed_fuel = 75 - cars[car]["fuel"]
        if needed_fuel < fuel:
            cars[car]["fuel"] = 75
            print(f"{car} refueled with {needed_fuel} liters")
        else:
            cars[car]["fuel"] += fuel
            print(f"{car} refueled with {fuel} liters")
    elif action == "Revert":
        car, kilometers = command.split(" : ")[1], int(command.split(" : ")[2])
        cars[car]["mileage"] -= kilometers
        if cars[car]["mileage"] >= 10000:
            print(f"{car} mileage decreased by {kilometers} kilometers")
        else:
            cars[car]["mileage"] = 10000
    command = input()
for car, info in cars.items():
    print(f"{car} -> Mileage: {info['mileage']} kms, Fuel in the tank: {info['fuel']} lt.")


################################################   Task Description   ################################################
# Problem 3 - Need for Speed III
# 
# Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
# Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2307#2.
# 
# You have just bought the latest and greatest computer game – Need for Seed III. 
# Pick your favorite cars and drive them all you want! We know that you can't wait to start playing.
# On the first line of the standard input, you will receive an integer n – the number of cars that you can obtain. 
# On the next n lines, the cars themselves will follow with their mileage and fuel available, 
# separated by "|" in the following format:
# "{car}|{mileage}|{fuel}"
# Then, you will be receiving different commands, each on a new line, separated by " : ", 
# until the "Stop" command is given:
#     • "Drive : {car} : {distance} : {fuel}":
#         o You need to drive the given distance, and you will need the given fuel to do that. 
#           If the car doesn't have enough fuel, print: "Not enough fuel to make that ride"
#         o If the car has the required fuel available in the tank, increase its mileage with the given distance, 
#           decrease its fuel with the given fuel, and print: 
#           "{car} driven for {distance} kilometers. {fuel} liters of fuel consumed."
#         o You like driving new cars only, so if a car's mileage reaches 100 000 km, 
#           remove it from the collection(s) and print: "Time to sell the {car}!"
#     • "Refuel : {car} : {fuel}":
#         o Refill the tank of your car. 
#         o Each tank can hold a maximum of 75 liters of fuel, so if the given amount of fuel is more 
#           than you can fit in the tank, take only what is required to fill it up. 
#         o Print a message in the following format: "{car} refueled with {fuel} liters"
#     • "Revert : {car} : {kilometers}":
#         o Decrease the mileage of the given car with the given kilometers and print the kilometers 
#           you have decreased it with in the following format:
#           "{car} mileage decreased by {amount reverted} kilometers"
#         o If the mileage becomes less than 10 000km after it is decreased, just set it to 10 000km and 
#           DO NOT print anything.
# Upon receiving the "Stop" command, you need to print all cars in your possession in the following format:
# "{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt."
# Input/Constraints
#     • The mileage and fuel of the cars will be valid, 32-bit integers, and will never be negative.
#     • The fuel and distance amounts in the commands will never be negative.
#     • The car names in the commands will always be valid cars in your possession.
# Output
#     • All the output messages with the appropriate formats are described in the problem description.
