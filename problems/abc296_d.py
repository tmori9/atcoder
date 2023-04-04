N, M = map(int, input().split())

ans = 10**18

# a < bを仮定する
for a in range(1, N + 1):
    b = M // a
    if not M % a == 0:  # 余りが発生した (掛け算してMに達しない) 場合は+1
        b += 1
    if b <= N:  # bはNを超えない
        ans = min(ans, a * b)
    if b < a:  # a<=b<=N に反する
        break

if ans == 10**18:
    print(-1)
else:
    print(ans)
