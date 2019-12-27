n = int(input())
ans = 0
a = 1
if n % 2 == 1:
    print(0)
else:
    for j in range(1,40):
        ans += (n // ((5**j)*10))
    n10 = n // 10
    print(ans+n10)