def calculation(operator, a, b):
    result = None
    if operator == "multiply":
        result = a * b
    elif operator == "divide":
        result = int(a / b)
    elif operator == "add":
        result = a + b
    elif operator == "subtract":
        result = a - b
    return result


operation = input()
parameter_a = int(input())
parameter_b = int(input())
print(calculation(operation, parameter_a, parameter_b))


################################################   Task Description   ################################################
# 3. Calculations
# Create a function that receives three parameters, calculates a result depending on the given operator, and returns it. 
# Print the result of the function.
# The input comes as three parameters – an operator as a string and two integer numbers. 
# The operator can be one of the following:  "multiply", "divide", "add", "subtract". 
