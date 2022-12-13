number_of_lines = int(input())
tank_capacity = 255
filled_capacity = 0
for lines in range(number_of_lines):
    current_liters = int(input())
    if (current_liters + filled_capacity) > tank_capacity:
        print("Insufficient capacity!")
    elif (current_liters + filled_capacity) <= tank_capacity:
        filled_capacity += current_liters
print(filled_capacity)


################################################   Task Description   ################################################
# 7. Water Overflow
# You have a water tank with a capacity of 255 liters. 
# On the first line, you will receive n – the number of lines, which will follow. 
# On the following n lines, you will receive liters of water (integers), which you should pour into your tank. 
# If the capacity is not enough, print "Insufficient capacity!" and continue reading the next line. 
# On the last line, print the liters in the tank.
