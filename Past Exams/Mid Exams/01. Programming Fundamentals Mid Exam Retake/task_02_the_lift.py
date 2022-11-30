people_waiting = int(input())
wagons_list = list(map(int, input().split()))
lift_capacity = len(wagons_list) * 4 - sum(wagons_list)

if lift_capacity < people_waiting:
    difference = people_waiting - lift_capacity
    wagons_list = [4] * len(wagons_list)
    print(f"There isn't enough space! {difference} people in a queue!")
else:
    for index, wagon in enumerate(wagons_list):
        if people_waiting == 0:
            break
        people_added = 0
        current_capacity = 0
        if wagon < 4:
            current_capacity = 4 - wagon
            if people_waiting <= current_capacity:
                people_added = people_waiting
                people_waiting = 0
            else:
                people_added = current_capacity
                people_waiting -= people_added
            wagons_list[index] += people_added

if people_waiting == 0:
    if wagons_list[-1] < 4:
        print("The lift has empty spots!")
print(*wagons_list)
