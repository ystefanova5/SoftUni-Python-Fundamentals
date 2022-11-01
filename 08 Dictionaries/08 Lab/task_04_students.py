# 04. Students
# Task Description:
# You will be receiving names of students, their ID, and a course of programming they have
# taken in the format "{name}:{ID}:{course}".
# On the last line, you will receive a name of a course in snake case lowercase letters.
# You should print only the information of the students who have taken the corresponding course
# in the format: "{name} - {ID}" on separate lines.
# Note: each student's ID will always be unique

students_id = {}
student_data = input().split(":")
while len(student_data) == 3:
    current_student = student_data[0]
    current_id = student_data[1]
    current_course = student_data[2]
    students_id[current_id] = [current_student, current_course]
    student_data = input().split(":")

course = student_data[0]
if "_" in course:
    course = course.replace("_", " ")
for key, value in students_id.items():
    if value[1] == course:
        print(f"{value[0]} - {key}")
