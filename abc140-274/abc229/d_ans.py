s = list(input())
k = int(input())

# 累積和
cumulative_sum = [0] * (len(s) + 1)

for i, value in enumerate(s):
    if value == ".":
        cumulative_sum[i + 1] = cumulative_sum[i] + 1
    else:
        cumulative_sum[i + 1] = cumulative_sum[i]

right = 0
ans = 0
for left, value in enumerate(s):
    while right < len(s) and cumulative_sum[right + 1] - cumulative_sum[left] <= k:
        right += 1
    ans = max(ans, right - left)

print(ans)