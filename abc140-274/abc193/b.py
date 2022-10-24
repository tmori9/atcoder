n = int(input())
sunuke_list = [list(map(int, input().split())) for i in range(n)]

min_money = 10000000000

for i, line in enumerate(sunuke_list):
    if line[2] - line[0] > 0:  # 購入可
        get_price = line[1]
        min_money = min(min_money, get_price)
if min_money == 10000000000:
    print(-1)
else:
    print(min_money)
