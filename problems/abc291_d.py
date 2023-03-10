n = int(input())
card_number = [list(map(int, input().split())) for i in range(n)]

MOD = 998244353

dp = [[0, 0] for _ in range(n)]
dp[0] = [1, 1]  # トランプ一枚の場合、表でも裏でも条件を満たす

for i in range(1, n):  # トランプ一枚は初期値で代入済み
    for pre in range(2):  # pre = 0 は一つ前のカードが表, pre = 1 は一つ前のカードが裏
        for now in range(2):  # now = 0 は現在のカードが表, now = 1は現在のカードが裏
            if card_number[i - 1][pre] != card_number[i][now]:
                dp[i][now] += dp[i - 1][pre]
    dp[i][0] = dp[i][0] % MOD
    dp[i][1] = dp[i][1] % MOD

print((dp[n - 1][0] + dp[n - 1][1]) % MOD)
