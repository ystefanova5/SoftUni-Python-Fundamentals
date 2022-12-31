from math import sqrt, floor


def longer_line(x1, y1, x2, y2, x3, y3, x4, y4):
    first_line_length = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    second_line_length = sqrt((x3 - x4) ** 2 + (y3 - y4) ** 2)
    longest_line = ""
    if first_line_length >= second_line_length:
        return [x1, y1, x2, y2]
    else:
        return [x3, y3, x4, y4]


def closest_point(lst):
    a1 = lst[0]
    b1 = lst[1]
    a2 = lst[2]
    b2 = lst[3]
    first_point_distance = sqrt(a1 ** 2 + b1 ** 2)
    second_point_distance = sqrt(a2 ** 2 + b2 ** 2)
    if first_point_distance <= second_point_distance:
        return f"({floor(a1)}, {floor(b1)})({floor(a2)}, {floor(b2)})"
    else:
        return f"({floor(a2)}, {floor(b2)})({floor(a1)}, {floor(b1)})"


input_x1 = float(input())
input_y1 = float(input())
input_x2 = float(input())
input_y2 = float(input())
input_x3 = float(input())
input_y3 = float(input())
input_x4 = float(input())
input_y4 = float(input())
print(closest_point(longer_line(input_x1, input_y1, input_x2, input_y2, input_x3, input_y3, input_x4, input_y4)))


################################################   Task Description   ################################################
# 3. Longer Line
# You will be given the coordinates of four points. The first and the second pair of points form two different lines. 
# Create a function that prints the longer line in the format "({X1}, {Y1})({X2}, {Y2})" 
# starting from the point which is closer to the center of the coordinate system (0, 0). 
# You can reuse the method that you wrote for the previous problem. 
# If the lines are of equal length, print only the first one. 
# The resulting coordinates must be formatted to the lower integer.
