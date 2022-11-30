first_receptionist_scope = int(input())
second_receptionist_scope = int(input())
third_receptionist_scope = int(input())
students_count = int(input())
hourly_capacity = first_receptionist_scope + second_receptionist_scope + third_receptionist_scope
counter = 0
time = 0
while students_count > 0:
    time += 1
    students_count -= hourly_capacity
    counter += 1
    if counter == 3 and students_count > 0:
        time += 1
        counter = 0
print(f"Time needed: {time}h.")