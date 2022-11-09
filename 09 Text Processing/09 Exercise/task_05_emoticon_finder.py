text = input()
for index, symbol in enumerate(text):
    if symbol == ":":
        if index + 1 < len(text):
            next_symbol = text[index + 1]
            if next_symbol != " ":
                result = symbol+next_symbol
                print(result)


################################################   Task Description   ################################################
# 5. Emoticon Finder
# Find all emoticons in the text. An emoticon always starts with ":" and is followed by a symbol.
# The input will be provided as a single string.
