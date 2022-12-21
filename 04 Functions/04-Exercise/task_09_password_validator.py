def password_validator(password):
    password_is_valid = True
    if not 6 <= len(password) <= 10:
        password_is_valid = False
        print("Password must be between 6 and 10 characters")
    for symbol in password:
        # following line can be replaced with: <if password.isalnum():>
        if (48 <= ord(symbol) <= 57) or (65 <= ord(symbol) <= 90) or (97 <= ord(symbol) <= 122):
            continue
        else:
            password_is_valid = False
            print("Password must consist only of letters and digits")
            break
    digit_counter = 0
    for symbol in password:
        if 48 <= ord(symbol) <= 57: # can be replaced with <if symbol.isdigit():>
            digit_counter += 1
    if digit_counter < 2:
        password_is_valid = False
        print("Password must have at least 2 digits")
    if password_is_valid:
        print("Password is valid")


user_password = input()
password_validator(user_password)


################################################   Task Description   ################################################
# 9. Password Validator
# Write a function that checks if a given password is valid. Password validations are:
#     • It should be 6 - 10 (inclusive) characters long
#     • It should consist only of letters and digits
#     • It should have at least 2 digits 
# If a password is valid, print "Password is valid".
# Otherwise, for every unfulfilled rule, print a message:
#     • "Password must be between 6 and 10 characters"
#     • "Password must consist only of letters and digits"
#     • "Password must have at least 2 digits"
