x, y, a, b = list(map(int,input().split()))

ans = 0

while True:
    if x*a <= x+b:
        if y <= x*a:
            ans += ((y-1-x)//b)
            break
        ans += 1
        x = x*a

    else:
        ans += ((y-1-x)//b)
        break

print(ans)
