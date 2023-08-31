n = int(input())
x = [list(map(int, input().split())) for i in range(n)]

INF = 10**18
current_aoki = 0
current_takahashi = 0
negaeri_cost = []  # [高橋に寝返るコスト, 獲得議席]
all_seats = 0  # 全議席数

for ku in x:
    takahashi, aoki, seat = ku
    all_seats += seat
    if takahashi > aoki:
        current_takahashi += seat
        negaeri_cost.append([0, 0])
    else:
        current_aoki += seat
        negaeri_cost.append([(aoki - takahashi + 1) // 2, seat])

# print(f"aoki = {current_aoki}")
# print(f"takahashi = {current_takahashi}")
# print(negaeri_cost)

# 必要な議席数
need_seats = (current_aoki - current_takahashi + 1) // 2
# print(f"必要議席数 = {need_seats}")

dp = [INF] * (all_seats + 1)
dp[0] = 0

for cost, seat in negaeri_cost:
    for i in range(all_seats, seat - 1, -1):
        dp[i] = min(dp[i], dp[i - seat] + cost)

ans = min(dp[need_seats:])
print(ans)
