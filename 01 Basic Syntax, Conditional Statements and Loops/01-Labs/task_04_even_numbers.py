number_count = int(input())
for i in range (number_count):
    number = int(input())
    all_numbers_are_even = True
    if number % 2 != 0:
        print(f"{number} is odd!")
        all_numbers_are_even = False
        break
    else:
        continue
if all_numbers_are_even:
    print("All numbers are even.")





