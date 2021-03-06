import math
n = int(input())


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


def multi_diff(es):
    return es == [es[0]] * len(es) if es else False


sum_num = 0
for i in range(1, n+1):
    yakusu_list = prime_factorize(i)
    if len(yakusu_list) >= 2 and multi_diff(yakusu_list):
        sum_num += 1

print(n-sum_num)
