usernames = input().split(", ")
for username in usernames:
    if 3 <= len(username) <= 16:
        modified_username = username.replace("-", "")
        modified_username = modified_username.replace("_", "")
        if modified_username.isalnum():
            print(username)


################################################   Task Description   ################################################
# 1. Valid Usernames
# Write a program that reads usernames on a single line (separated by ", ") 
# and prints all valid usernames on separate lines. 
# A valid username:
# • has length between 3 and 16 characters inclusive
# • can contain only letters, numbers, hyphens, and underscores
# • has no redundant symbols before, after, or in between
