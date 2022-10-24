import math
a,b,x=map(int,input().split())
x_2d = x/a
if a*a*b == x:
    print(0)
    exit()
if x/a > (a*b)/2:
    print(90-math.degrees(math.atan(a/(2*b-2*x/(a*a)))))
else:
    print(math.degrees(math.atan(b/(2*x/(a*b)))))