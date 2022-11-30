def swap(list_name, index1, index2):
    list_name[index1], list_name[index2] = list_name[index2], list_name[index1]
    return list_name


def multiply(list_name, index1, index2):
    list_name[index1] = list_name[index1] * list_name[index2]
    return list_name


def decrease(list_name):
    result_list = [x - 1 for x in list_name]
    return result_list


numbers = list(map(int, input().split()))
command = input()
while command != "end":
    current_command = command.split()[0]
    if current_command == "swap":
        first_index = int(command.split()[1])
        second_index = int(command.split()[2])
        numbers = swap(numbers, first_index, second_index)
    elif current_command == "multiply":
        first_index = int(command.split()[1])
        second_index = int(command.split()[2])
        numbers = multiply(numbers, first_index, second_index)
    elif current_command == "decrease":
        numbers = decrease(numbers)
    command = input()
result = [str(x) for x in numbers]
print(", ".join(result))
