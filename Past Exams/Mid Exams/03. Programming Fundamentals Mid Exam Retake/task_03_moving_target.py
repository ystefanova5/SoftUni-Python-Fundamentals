def shoot(list_name, index, power):
    if index in range(len(list_name)):
        if list_name[index] > power:
            list_name[index] = list_name[index] - power
        else:
            list_name.pop(index)
    return list_name


def add(list_name, index, value):
    message = None
    if index in range(len(list_name)):
        list_name.insert(index, value)
    else:
        message = "Invalid placement!"
    return list_name, message


def strike(list_name, index, radius):
    message = None
    result_list = []
    if index in range(len(list_name)) and \
            index + radius in range(len(list_name)) and \
            index - radius in range(len(list_name)):
        for i, value in enumerate(list_name):
            if i not in range(index - radius, index + radius + 1):
                result_list.append(value)
    else:
        message = "Strike missed!"
        result_list = list_name
    return result_list, message


targets = list(map(int, input().split()))
command = input()
while command != "End":
    current_command = command.split()
    action = current_command[0]
    first_value = int(current_command[1])
    second_value = int(current_command[2])
    if action == "Shoot":
        targets = shoot(targets, first_value, second_value)
    elif action == "Add":
        targets, add_text = add(targets, first_value, second_value)
        if add_text is not None:
            print(add_text)
    elif action == "Strike":
        targets, strike_text = strike(targets, first_value, second_value)
        if strike_text is not None:
            print(strike_text)
    command = input()
targets = [str(x) for x in targets]
print("|".join(targets))
