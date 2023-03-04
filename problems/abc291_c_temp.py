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


for i, s in enumerate(s_list):
    if s == "R":
        x += 1
        if x in x_set:
            same_line = True
        else:
            same_line = False
        x_set.add(x)
    elif s == "L":
        x -= 1
        if x in x_set:
            same_line = True
        else:
            same_line = False
        x_set.add(x)

    elif s == "U":
        y += 1
        if y in y_set:
            same_row = True
        else:
            same_row = False
        y_set.add(y)

    else:
        y -= 1
        if y in y_set:
            same_row = True
        else:
            same_row = False
        y_set.add(y)

    print(same_line)
    print(same_row)
    if same_line and same_row and not i == 0:
        print("Yes")
        exit()
print("No")
