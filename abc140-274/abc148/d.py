N=int(input())
bricks=list(map(int,input().split()))

manzoku=1
hakai = 0
for i in range(N):
    if bricks[i] == manzoku:
        manzoku += 1
    else:
        hakai += 1

if hakai == N:
    print(-1)
else: 
    print(hakai)
        

