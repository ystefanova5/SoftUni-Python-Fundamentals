first_string = input()
second_string = input()
last_word = first_string
for string_index in range(len(first_string)):
    new_word = second_string[:string_index + 1] + first_string[string_index + 1:]
    if new_word == last_word:
        continue
    else:
        last_word = new_word
        print(new_word)