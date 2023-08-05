n, m = map(int, input().split())
comp = [list(map(int, input().split())) for i in range(m)]

s = set(range(1, n + 1))

for first, second in comp:
    s.discard(second)

if len(s) == 1:
    print(s.pop())
else:
    print(-1)
