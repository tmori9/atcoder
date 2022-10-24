n, x, y = map(int, input().split())
a_list = list(map(int, input().split()))

dp_x = [False] * 20001
dp_y = [False] * 20001

dp_x[0] = True
print(dp_x[:5])
