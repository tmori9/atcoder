from math import sqrt
a,b,c=map(int,input().split())

if a+b+2.0*sqrt(a*b) < c:
    print("Yes")
else:
    print("No")
