h, w = map(int, input().split())
x = [list(map(str, input())) for i in range(h)]

x_reverse = list(zip(*x))

count_list = []
for one_line in x_reverse:
    count = 0
    for val in one_line:
        if val == "#":
            count += 1
    count_list.append(count)

print(*count_list)