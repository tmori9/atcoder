from collections import Counter

n = int(input())
int_list = list(map(int, input().split()))

"""nを素因数分解"""
"""2以上の整数n => [[素因数, 指数], ...]の2次元リスト"""


def factorization(n):
    # arr = []
    arr_dict = {}
    temp = n
    for i in range(2, int(-(-(n**0.5) // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            # arr.append([i, cnt])
            arr_dict[i] = cnt

    if temp != 1:
        # arr.append([temp, 1])
        arr_dict[temp] = 1

    if arr_dict == {}:
        # arr.append([n, 1])
        arr_dict[n] = 1

    return Counter(arr_dict)


print(factorization(24))

counter_list = []
for one_num in int_list:
    counter_list.append(factorization(one_num))
print(counter_list)
