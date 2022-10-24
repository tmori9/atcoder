l, r, d = map(int, input().split())

result_sum = 0
for i in range(l,r+1):
    if i % d == 0:
        result_sum += 1

print(result_sum)