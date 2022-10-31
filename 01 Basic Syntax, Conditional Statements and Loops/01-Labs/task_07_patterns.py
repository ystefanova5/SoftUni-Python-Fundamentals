# 07. Patterns
# Task Description:
# Write a program that receives a number and creates the following pattern. 
# The number represents the largest count of stars on one row.


max_stars = int(input())
for first_stars in range(max_stars):
    print("*" * (first_stars + 1))

for second_stars in range(max_stars - 1, -1, -1):
    print("*" * (second_stars))
