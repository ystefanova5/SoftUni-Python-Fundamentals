number_of_people = int(input())
capacity = int(input())
courses = int(number_of_people / capacity)
if capacity > number_of_people:
    courses = 1
else:
    if number_of_people % capacity != 0:
        courses += 1
print(courses)


################################################   Task Description   ################################################
# 3. Elevator
# Calculate how many courses will be needed to elevate N persons by using an elevator with a capacity of P persons. 
# The input holds two lines: the number of people N and the capacity P of the elevator.
