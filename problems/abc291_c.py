n = int(input())
s_list = list(input())

same_line = True  # 横
same_row = True  # 縦

r_count = 0
l_count = 0
u_count = 0
d_count = 0

x = 0
y = 0
x_set = set([0])
y_set = set([0])

current = (x, y)
all_set = {current}

for i, s in enumerate(s_list):
    if s == "R":
        x += 1
        if (x, y) in all_set:
            print("Yes")
            exit()
        all_set.add((x, y))
    elif s == "L":
        x -= 1
        if (x, y) in all_set:
            print("Yes")
            exit()
        all_set.add((x, y))

    elif s == "U":
        y += 1
        if (x, y) in all_set:
            print("Yes")
            exit()
        all_set.add((x, y))

    else:
        y -= 1
        if (x, y) in all_set:
            print("Yes")
            exit()
        all_set.add((x, y))

print("No")
