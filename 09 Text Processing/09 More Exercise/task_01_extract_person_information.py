def get_name_and_age(sentence):
    name_first_index = sentence.index("@") + 1
    name_last_index = sentence.index("|")
    age_first_index = sentence.index("#") + 1
    age_last_index = sentence.index("*")
    name = sentence[name_first_index:name_last_index]
    age = sentence[age_first_index:age_last_index]
    return name, age


number_of_entries = int(input())
for sentence in range(number_of_entries):
    current_sentence = input()
    current_name, current_age = get_name_and_age(current_sentence)
    print(f"{current_name} is {current_age} years old.")

################################################   Task Description   ################################################
# 1. Extract Person Information
# Write a program that reads N lines of strings and extracts the name and the age of a given person:
# • The person's name will be surrounded by "@" and "|" in the format "@{name}|".
# • The person's age will be surrounded by "#" and "*" in the format "#{age}*".
# Example: "Hello my name is @Peter| and I am #20* years old." 
# For each found name-age pair, print a line in the following format "{name} is {age} years old."
