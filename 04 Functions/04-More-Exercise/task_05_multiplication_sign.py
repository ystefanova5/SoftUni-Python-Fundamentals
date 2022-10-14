def positive_or_negative(first, second, third):
    numbers = [first, second, third]
    zero = 0
    negative = 0
    positive = 0
    for num in numbers:
        if num > 0:
            positive += 1
        elif num == 0:
            zero += 1
        else:
            negative += 1
    if zero > 0:
        return "zero"
    else:
        if negative == 1 or negative == 3:
            return "negative"
        else:
            return "positive"


first_num = int(input())
second_num = int(input())
third_num = int(input())
print(positive_or_negative(first_num, second_num, third_num))
