def find_numbers(list_name):
    list_average = sum(list_name) / len(list_name)
    result_list = [x for x in list_name if x > list_average]
    result_list = sorted(result_list, reverse=True)
    result_list = [str(x) for x in result_list]
    if len(result_list) > 5:
        result_list = result_list[:5]
    if len(result_list) == 0:
        return "No"
    else:
        return " ".join(result_list)


numbers = list(map(int, input().split()))
print(find_numbers(numbers))
