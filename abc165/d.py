import math
a,b,n = map(int, input().split())

if n>=b-1:
    test = math.floor(a*(b-1)/b) - a * math.floor((b-1)/b)
else:
    test = math.floor(a*n/b) - a * math.floor(n/b)
print(test)