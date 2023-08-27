n = int(input())
x = [list(map(int, input().split())) for i in range(n)]

current_aoki = 0
current_takahashi = 0
negaeri_cost = []  # [高橋に寝返るコスト, 獲得議席]

for ku in x:
    takahashi, aoki, zaseki = ku
    if takahashi > aoki:
        current_takahashi += zaseki
    else:
        current_aoki += zaseki
        negaeri_cost.append([(aoki - takahashi) // 2 + 1, zaseki])

print(f"aoki = {current_aoki}")
print(f"takahashi = {current_takahashi}")
print(negaeri_cost)

# 必要な議席数
need_zaseki = (current_aoki - current_takahashi) // 2 + 1
print(f"need_zaseki = {need_zaseki}")

dp = [[0] * (len(negaeri_cost) + 1) for j in range(need_zaseki + 1)]

for i in range(len(negaeri_cost)):
    for j in range(need_zaseki + 1):
        if j < negaeri_cost[i][0]:
            dp[j][i + 1] = dp[j][i]
        else:
            dp[j][i + 1] = max(
                dp[j][i], dp[j - negaeri_cost[i][0]][i] + negaeri_cost[i][1]
            )
print(dp)
