current_number = float(input())
number_is_in_range = False
while not number_is_in_range:
    if 1 <= current_number <= 100:
        number_is_in_range = True
        print(f"The number {current_number} is between 1 and 100")
        break
    else:
        current_number = float(input())
