def get_damage(left_list, right_list, type, treshold):
    if type == "cheap":
        left_list = [x for x in left_list if x < treshold]
        right_list = [x for x in right_list if x < treshold]
    elif type == "expensive":
        left_list = [x for x in left_list if x >= treshold]
        right_list = [x for x in right_list if x >= treshold]
    items_position = ""
    largest_sum = 0
    if sum(left_list) >= sum(right_list):
        items_position = "Left"
        largest_sum = sum(left_list)
    else:
        items_position = "Right"
        largest_sum = sum(right_list)
    return items_position, largest_sum


price_ratings = list(map(int, input().split(", ")))
entry_point = int(input())
item_type = input()
entry_point_item = price_ratings[entry_point]
damage_left = price_ratings[:entry_point]
damage_right = price_ratings[entry_point + 1:]
position, sum_damage = get_damage(damage_left, damage_right, item_type, entry_point_item)

print(f"{position} - {sum_damage}")
