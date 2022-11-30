days_in_month = 30
food_kgs = float(input())
hay_kgs = float(input())
cover_kgs = float(input())
guinea_weight = float(input())
everything_is_fine = True

for day in range(1, days_in_month + 1):
    if food_kgs / 0.300 == 30:
        everything_is_fine = False
        break
    food_kgs -= 0.300
    if food_kgs < 0:
        everything_is_fine = False
        break
    if day % 2 == 0:
        added_hay = food_kgs * 0.05
        hay_kgs -= (food_kgs * 0.05)
        if hay_kgs < 0:
            everything_is_fine = False
            break
    if day % 3 == 0:
        cover_kgs -= guinea_weight / 3
        if cover_kgs < 0:
            everything_is_fine = False
            break
if everything_is_fine:
    print(f"Everything is fine! Puppy is happy! Food: {food_kgs:.2f}, Hay: {hay_kgs:.2f}, Cover: {cover_kgs:.2f}.")
else:
    print("Merry must go to the pet store!")
