max_stars = int(input())
for first_stars in range(max_stars):
    print("*" * (first_stars + 1))

for second_stars in range(max_stars - 1, -1, -1):
    print("*" * (second_stars))
