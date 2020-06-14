[N,K] = list(map(int,input().split()))
A = list(map(int,input().split()))

for j in range(min(K,50)):
    NextA = [0]*N
    for i in range(N):
        l = max(0, i-A[i])
        r = min(N-1, i+A[i])

        NextA[l]+=1
        if r+1<=N-1:
            NextA[r+1]-=1

    for i in range(1,N):
        NextA[i] += NextA[i-1]
    A = NextA[:]

print(*NextA)
