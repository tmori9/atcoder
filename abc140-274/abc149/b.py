a,b,k=map(int, input().split())

if a<=k:
    k = k-a
    a=0
else:
    a = a-k
    print(a,b)
    exit()
    
if b<=k:
    b = k-b
    b=0
else:
    b = b-k
    print(a,b)
    exit()

print(a,b)
