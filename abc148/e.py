N=int(input())

def f(n):
    if n<2:
        return 1
    else:
        if n % 10 != 0:
            return f(n-2)
        else:
            return n*f(n-2)

if N%2==0:
    print(f(N))
else:
    print(0)

"""
if N%2==0:
    pass
else:
    print(0)
    exit()

result = 0
for i in range(N, 0, -2):
    if i%10 == 0:
        result +=1
    if i%50 == 0:
        result +=1

print(result)
"""
