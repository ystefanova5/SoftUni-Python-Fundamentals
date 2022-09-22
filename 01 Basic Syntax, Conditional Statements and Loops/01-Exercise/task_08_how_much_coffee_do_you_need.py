command = input()
event_list_lowercase = ["coding", "dog", "cat", "movie"]
event_list_uppercase = ["CODING", "DOG", "CAT", "MOVIE"]
number_of_coffees = 0
while command != "END":
    event = command
    if event in event_list_lowercase:
        number_of_coffees += 1
    elif event in event_list_uppercase:
        number_of_coffees += 2
    command = input()
if number_of_coffees <= 5:
    print(number_of_coffees)
else:
    print("You need extra sleep")