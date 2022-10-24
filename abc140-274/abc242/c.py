n = int(input())

dp = []  # dp[桁数][0-8]
dp.append([2, 3, 3, 3, 3, 3, 3, 3, 2])  # 2桁目の個数 (i=0)

mod_n = 998244353

for i in range(1, 1000000):
    maked_list = []
    maked_list.append((dp[i - 1][0] + dp[i - 1][1]) % mod_n)
    maked_list.append((dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % mod_n)
    maked_list.append((dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][3]) % mod_n)
    maked_list.append((dp[i - 1][2] + dp[i - 1][3] + dp[i - 1][4]) % mod_n)
    maked_list.append((dp[i - 1][3] + dp[i - 1][4] + dp[i - 1][5]) % mod_n)
    maked_list.append((dp[i - 1][4] + dp[i - 1][5] + dp[i - 1][6]) % mod_n)
    maked_list.append((dp[i - 1][5] + dp[i - 1][6] + dp[i - 1][7]) % mod_n)
    maked_list.append((dp[i - 1][6] + dp[i - 1][7] + dp[i - 1][8]) % mod_n)
    maked_list.append((dp[i - 1][7] + dp[i - 1][8]) % mod_n)
    dp.append(maked_list)
print(sum(dp[n - 2]) % mod_n)
