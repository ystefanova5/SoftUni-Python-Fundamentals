number = int(input())
number_is_prime = True
for n in range(2, number):
    if number % n == 0:
        number_is_prime = False
        break
print(number_is_prime)