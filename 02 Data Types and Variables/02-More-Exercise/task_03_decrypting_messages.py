key = int(input())
number_of_lines = int(input())
for _ in range(number_of_lines):
    input_letter = input()
    output_letter = chr(ord(input_letter) + key)
    print(output_letter, end="")