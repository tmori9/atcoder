n, x = map(int, input().split())
a_list = list(map(int, input().split()))
a_list.sort()

# 先頭に0を追加したと仮定する
if sum(a_list[:-1]) >= x:
    print(0)
    exit()

if sum(a_list[1:]) < x:
    print(-1)
    exit()
else:
    print(x - sum(a_list[1:-1]))
