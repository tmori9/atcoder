n, x, y = map(int, input().split())
a_list = list(map(int, input().split()))

dp_x = set([0])
dp_y = set([0])


for i, Ai in enumerate(a_list):
    dp_x_temp = set()
    dp_y_temp = set()

    if i % 2 == 0:  # 偶数 (x移動)
        for val in dp_x:
            if i == 0:
                dp_x_temp.add(val + Ai)
            else:
                dp_x_temp.add(val + Ai)
                dp_x_temp.add(val - Ai)
        dp_x = dp_x_temp

    else:  # 奇数 (y移動)
        for val in dp_y:
            dp_y_temp.add(val + Ai)
            dp_y_temp.add(val - Ai)
        dp_y = dp_y_temp

if x in dp_x and y in dp_y:
    print("Yes")
else:
    print("No")
