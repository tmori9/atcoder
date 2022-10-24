x, y, z = map(int, input().split())

x_plus = False if x <= 0 else True
y_plus = False if y <= 0 else True
z_plus = False if z <= 0 else True

res = 0
if not x_plus == y_plus:  # そのまま到達可能
    res = abs(x)
else:
    if abs(x) <= abs(y):  # 壁の手前にゴールがある
        res = abs(x)
    else:
        if y_plus == z_plus and abs(y) <= abs(z):  # ゴールの奥にハンマーがある
            res = -1
        else:
            if not x_plus == z_plus:
                res = abs(z) * 2 + abs(x)
            else:
                res = abs(x)

print(res)
