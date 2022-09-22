number = int(input())
happy_year = 0
year_is_happy = False
current_year = number + 1
while not year_is_happy:
    if len(set(str(current_year))) == len(str(number)):
        happy_year = current_year
        year_is_happy = True
    else:
        current_year += 1
if year_is_happy:
    print(happy_year)