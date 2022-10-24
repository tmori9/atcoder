a, b, c, x = map(int, input().split())
if x <= a:
    print(1.000000000000)
    exit()
elif x > b:
    print(0.000000000000)
else:
    ans = c / (b - a)
    print(ans)
