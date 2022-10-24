A,B=map(int,input().split())
cf = [1]

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def is_prime(n):
    for i in range(2, n + 1):
        if i * i > n:
            break
        if n % i == 0:
            return False
    return n != 1

for i in range(2, min(A,B)+1):
    if A%i == 0 and B%i == 0:
        cf.append(i)
count = 1
for i in cf:
    if not i==2 and i%2==0:
        continue
    if is_prime(i):
        count += 1
print(count)
