from bisect import bisect_right

n, m, p = map(int, input().split())
a_list = sorted(list(map(int, input().split())))
b_list = sorted(list(map(int, input().split())))


res_sum = 0

cumulative_sum_b = [0]
for b in b_list:
    cumulative_sum_b.append(cumulative_sum_b[-1] + b)

for a_i, a in enumerate(a_list):
    if a >= p:
        res_sum += p * (n - a_i) * m
        break

    b_i = bisect_right(b_list, p - a)
    res_sum += a * b_i + cumulative_sum_b[b_i]
    res_sum += p * (m - b_i)
print(res_sum)
