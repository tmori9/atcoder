n, x, y = map(int, input().split())
a_list = list(map(int, input().split()))

dp_x = [False] * 20002
dp_y = [False] * 20002

dp_x[10000] = True
dp_y[10000] = True

for i, Ai in enumerate(a_list):
    dp_x_temp = [False] * 20002
    dp_y_temp = [False] * 20002

    if i % 2 == 0:  # 偶数 (x移動)
        for j in range(len(dp_x)):
            if i == 0:
                if dp_x[j] == True:
                    dp_x_temp[j + Ai] = True
            else:
                if dp_x[j] == True:
                    dp_x_temp[j + Ai] = True
                    dp_x_temp[j - Ai] = True
        dp_x = dp_x_temp

    else:  # 奇数 (y移動)
        for j in range(len(dp_y)):
            if dp_y[j] == True:
                dp_y_temp[j + Ai] = True
                dp_y_temp[j - Ai] = True

        dp_y = dp_y_temp

if dp_x[10000 + x] == True and dp_y[10000 + y] == True:
    print("Yes")
else:
    print("No")
