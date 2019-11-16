from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

x,y=map(int,input().split())

if not(-(-x//2) <= y and y <= x*2):
    print(0)
    exit()

flag = True

count = 0
while flag:
    count += 1
    x += 1
    y -= 1

    if y*2 == x: # yC0
        print(cmb(y, count)%1000000007)
        exit()
    if y*2 < x: # ない
        print(0)
        exit()


 