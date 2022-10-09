operation = input()
parameter_a = int(input())
parameter_b = int(input())


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


print(calculation(operation, parameter_a, parameter_b))
