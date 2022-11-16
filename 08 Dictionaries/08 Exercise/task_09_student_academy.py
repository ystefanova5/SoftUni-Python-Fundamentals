number_of_students = int(input())
counter = 0
students_list = []
students_dict = {}
for student in range(number_of_students * 2):
    data = input()
    students_list.append(data)
for index, element in enumerate(students_list):
    if index % 2 == 0:
        current_value = float(students_list[index + 1])
        if element not in students_dict:
            students_dict[element] = []
        students_dict[element].append(current_value)
for student, grades in students_dict.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.50:
        print(f"{student} -> {average_grade:.2f}")
        

################################################   Task Description   ################################################
# 9. Student Academy
# Write a program that keeps the information about students and their grades.
# On the first line, you will receive an integer number representing the next pair of rows.
# On the next lines, you will be receiving each student's name and their grade.
# Keep track of all grades for each student and keep only the students
# with an average grade higher than or equal to 4.50.
# Print the final dictionary with students and their average grade in the following format:
# "{name} -> {averageGrade}"
# Format the average grade to the 2nd decimal place.
