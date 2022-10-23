numbers = list(map(int, input().split()))
command = input()
while command != "Finish":
    current_command = command.split()[0]
    value = int(command.split()[1])
    if current_command == "Add":
        numbers.append(value)
    elif current_command == "Remove":
        if value in numbers:
            numbers.remove(value)
    elif current_command == "Replace":
        replacement = int(command.split()[2])
        if value in numbers:
            for index, num in enumerate(numbers):
                if num == value:
                    numbers[index] = replacement
                    break
    elif current_command == "Collapse":
        numbers = [x for x in numbers if x >= value]
    command = input()
print(*numbers)