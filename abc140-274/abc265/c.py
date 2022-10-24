h, w = map(int, input().split())

x = [list(map(str, input())) for i in range(h)]

pt_h = 0
pt_w = 0
exit_set = set()

while True:
    if pt_h * 1000 + pt_w in exit_set:
        print(-1)
        exit()
    exit_set.add(pt_h * 1000 + pt_w)

    if x[pt_h][pt_w] == "R":
        pt_w += 1
        if pt_w >= len(x[0]):
            print(f"{pt_h+1} {pt_w}")
            exit()
    elif x[pt_h][pt_w] == "L":
        pt_w -= 1
        if pt_w <= -1:
            print(f"{pt_h+1} {pt_w+2}")
            exit()
    elif x[pt_h][pt_w] == "D":
        pt_h += 1
        if pt_h >= len(x):
            print(f"{pt_h} {pt_w+1}")
            exit()
    elif x[pt_h][pt_w] == "U":
        pt_h -= 1
        if pt_h <= -1:
            print(f"{pt_h+2} {pt_w+1}")
            exit()
