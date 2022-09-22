start_index = int(input())
end_index = int(input())
for character in range(start_index, end_index + 1):
    current_character = chr(character)
    print(current_character, end=" ")
