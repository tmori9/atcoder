x, y, n = map(int, input().split())

if x * 3 <= y:  # 全部x円1個で買う
    print(n * x)
else:  # 最大値までy円3個で買い、残った個数をx円1個で買う
    y_count = n // 3
    x_count = n % 3
    print(y * y_count + x * x_count)
