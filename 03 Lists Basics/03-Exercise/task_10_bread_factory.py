day_events = input()
energy = 100
coins = 100
day_events_list = day_events.split("|")
day_is_completed = True
for i in range(len(day_events_list)):
    current_event_string = day_events_list[i]
    current_event_list = current_event_string.split("-")
    current_event = current_event_list[0]
    current_value = int(current_event_list[1])
    if current_event == "rest":
        gained_energy = 0
        if energy >= 100:
            gained_energy = 0
        else:
            energy += current_value
            if energy > 100:
                gained_energy = current_value + (100 - energy)
                energy = 100
            else:
                gained_energy = current_value
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")
    elif current_event == "order":
        if (energy - 30) >= 0:
            energy -= 30
            coins += current_value
            print(f"You earned {current_value} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if (coins - current_value) >= 0:
            coins -= current_value
            print(f"You bought {current_event}.")
        else:
            print(f"Closed! Cannot afford {current_event}.")
            day_is_completed = False
            break
if day_is_completed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")


################################################   Task Description   ################################################
# 10. * Bread Factory
# As a young baker, you are baking the bread out of the bakery. 
# You have initial energy 100 and initial coins 100. You will be given a string representing the working day events. 
# Each event is separated with '|' (vertical bar): "event1|event2| … eventN"
# Each event contains an event name or an ingredient and a number, separated by a dash ("{event/ingredient}-{number}")
#     • If the event is "rest":
#         o You gain energy (the number in the second part). Note: your energy cannot exceed your initial energy (100). 
#           Print: "You gained {gained_energy} energy.". 
#         o After that, print your current energy: "Current energy: {current_energy}.".
#     • If the event is "order": 
#         o You've earned some coins (the number in the second part). 
#         o Each time you get an order, your energy decreases by 30 points.
#  If you have the energy to complete the order, print: "You earned {earned} coins.".
#  Otherwise, skip the order and gain 50 energy points. Print: "You had to rest!".
#     • In any other case, you have an ingredient you should buy. 
#       The second part of the event contains the coins you should spend. 
#         o If you have enough money, you should buy the ingredient and print:
#           "You bought {ingredient}."
#         o Otherwise, print "Closed! Cannot afford {ingredient}." and your bakery rush is over. 
# If you managed to handle all events throughout the day, print on the following 3 lines: 
# "Day completed!"
# "Coins: {coins}"
# "Energy: {energy}"
# Input / Constraints
# You will receive a string representing the working day events, separated with '|' (vertical bar) in the format:
# "event1|event2| … eventN".
# Each event contains an event name or an ingredient and a number, 
# separated by a dash in the format: "{event/ingredient}-{number}"
# Output
# Print the corresponding messages described above.
