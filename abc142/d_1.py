A,B=map(int,input().split())
def sieve(n):
    is_prime = [True for _ in range(n+1)]
    is_prime[0] = False

    for i in range(2, n+1):
        if is_prime[i-1]:
            j = 2 * i
            while j <= n:
                is_prime[j-1] = False
                j += i
    table = [ i for i in range(1, n+1) if is_prime[i-1] and n%i==0]
    return table
A_cf = sieve(A)
B_cf = sieve(B)
cf = []
for i in A_cf:
    for j in B_cf:
        if i==j:
            cf.append(i)
print(len(cf)+1)