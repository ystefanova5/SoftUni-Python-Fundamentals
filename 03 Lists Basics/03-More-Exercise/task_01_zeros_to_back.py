input_string = input()
zeros_counter = 0
numbers_list = input_string.split(", ")
final_list = []
for item in numbers_list:
    if item == "0":
        zeros_counter += 1
    else:
        final_list.append(int(item))
for zeros in range(zeros_counter):
    final_list.append(int(0))
print(final_list)
