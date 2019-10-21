N = int(input())
B = list(map(int, input().split()))
A= [100000]*N

for i, b in enumerate(B):
    if A[i] >= b:
        A[i] = b
    if A[i+1] >= b:
        A[i+1] = b

print(sum(A))