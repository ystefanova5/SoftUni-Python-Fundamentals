from math import ceil

students_number = int(input())
lectures_number = int(input())
additional_bonus = int(input())

all_bonuses = []
all_attendances = []

for count_students in range(students_number):
    student_attendance = int(input())
    total_bonus = student_attendance / lectures_number * (5 + additional_bonus)
    all_bonuses.append(total_bonus)
    all_attendances.append(student_attendance)

if students_number == 0 or lectures_number == 0:
    max_bonus = 0
    attendance_of_max_bonus = 0
else:
    max_bonus = max(all_bonuses)
    index_max_bonus = all_bonuses.index(max_bonus)
    attendance_of_max_bonus = all_attendances[index_max_bonus]

print(f"Max Bonus: {ceil(max_bonus)}.")
print(f"The student has attended {attendance_of_max_bonus} lectures.")
