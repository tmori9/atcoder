n = int(input())
p = list(map(int, input().split()))

if len(p) == 1:
    print(0)
else:
    print(max(0, max(p[1:]) + 1 - p[0]))
