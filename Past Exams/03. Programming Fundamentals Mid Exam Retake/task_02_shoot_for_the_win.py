targets_list = list(map(int, input().split()))
shot_targets_count = 0
command = input()
while command != "End":
    index = int(command)
    if index in range(len(targets_list)):
        if targets_list[index] != -1:
            shot_target = targets_list[index]
            for i, target in enumerate(targets_list):
                if i != index and target != -1 and target > shot_target:
                    targets_list[i] -= shot_target
                elif i != index and target != -1 and target <= shot_target:
                    targets_list[i] += shot_target
            shot_targets_count += 1
            targets_list[index] = -1
    command = input()
print(f"Shot targets: {shot_targets_count} ->", end=" ")
print(*targets_list)
