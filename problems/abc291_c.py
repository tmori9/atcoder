n = int(input())
command_list = list(input())


moved_position = {(0, 0)}  # 移動済みの座標
now_position = [0, 0]

for command in command_list:
    if command == "R":
        now_position[0] += 1
    elif command == "L":
        now_position[0] -= 1
    elif command == "U":
        now_position[1] += 1
    else:
        now_position[1] -= 1

    if tuple(now_position) in moved_position:
        print("Yes")
        exit()
    moved_position.add(tuple(now_position))

print("No")
