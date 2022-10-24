import collections

n = int(input())
x_list = list(map(int, input().split()))


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors


def prime_decomposition(n):
    i = 2
    table = []
    while i * i <= n:
        while n % i == 0:
            n /= i
            table.append(i)
        i += 1
    if n > 1:
        table.append(int(n))
    return table


x_set = set()
x_nokori_set = []
for i in x_list:
    temp_list = prime_decomposition(i)
    temp_set = set(temp_list)
    if len(temp_set) == 1:
        x_set.add(temp_list[0])
    else:
        x_nokori_set.append(temp_list)

while True:
    temp_first = []
    for i in x_nokori_set:
        temp_set = set(i)
        is_flag = False
        for j in temp_set:
            if j in x_set:
                is_flag = True

        if not(is_flag):
            temp_first.extend(i)
    if len(temp_first) == 0:
        break
    else:
        c = collections.Counter(temp_first)
        x_set.add(c.most_common()[0][0])


result = 1
for j in list(x_set):
    result = result * j
print(result)
