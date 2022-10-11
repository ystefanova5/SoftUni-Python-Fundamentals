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