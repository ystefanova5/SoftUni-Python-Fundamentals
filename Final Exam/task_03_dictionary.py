words = input().split(" | ")
dictionary = {}
for item in words:
    word, definition = item.split(": ")
    if word not in dictionary:
        dictionary[word] = []
    dictionary[word].append(definition)
test_words = input().split(" | ")
command = input()
if command == "Test":
    for test_word in test_words:
        if test_word in dictionary:
            print(f"{test_word}:")
            for value in dictionary[test_word]:
                print(f" -{value}")
elif command == "Hand Over":
    print(*dictionary.keys())


################################################   Task Description   ################################################
# 3. Dictionary
