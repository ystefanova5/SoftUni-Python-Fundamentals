def get_loading_status(number):
    if number == 100:
        print("100% Complete!")
        print("[%%%%%%%%%%]")
    else:
        symbol_count = number // 10
        symbol = "%"
        dots = "."
        print(f"{number}% [{symbol_count*symbol}{(10-symbol_count)*dots}]")
        print("Still loading...")


input_number = int(input())
get_loading_status(input_number)


################################################   Task Description   ################################################
# 11. * Loading Bar
# You will receive a single integer number between 0 and 100 (inclusive) 
# divisible by 10 without remainder (0, 10, 20, 30...). 
# Your task is to create a function that returns a loading bar depending on the number you have received in the input. 
# Print the result on the console. For more clarification, see the examples below.
