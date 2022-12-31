from math import sqrt, floor


def closest_point(x1, y1, x2, y2):
    first_point_distance = sqrt(x1 ** 2 + y1 ** 2)
    second_point_distance = sqrt(x2 ** 2 + y2 ** 2)
    if first_point_distance <= second_point_distance:
        return f"({floor(x1)}, {floor(y1)})"
    else:
        return f"({floor(x2)}, {floor(y2)})"


input_x1 = float(input())
input_y1 = float(input())
input_x2 = float(input())
input_y2 = float(input())
print(closest_point(input_x1, input_y1, input_x2, input_y2))


################################################   Task Description   ################################################
# 2. Center Point
# You will be given the coordinates of two points 
# on a Cartesian coordinate system - X1, Y1, X2, and Y2 on separate lines. 
# Write a function that prints the point which is closest to the center 
# of the coordinate system (0, 0) in the format: "({X}, {Y})"
# If the points are at the same distance from the center, print only the first one. 
# The resulting coordinates must be formatted to the lower integer.
