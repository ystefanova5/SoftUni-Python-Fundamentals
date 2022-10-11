def check_palindrome(number):
    if number == number[::-1]:
        return True
    else:
        return False


list_of_integers = input().split(", ")
for element in list_of_integers:
    print(check_palindrome(element))
