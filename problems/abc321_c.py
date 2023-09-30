from itertools import combinations

k = int(input())

# リストは0桁目を最上位とする
# 例: 123 = [1, 2, 3]


digits = 10
res = 1

usable_digits = list(range(10))
# print(usable_digits)

for d in range(1, digits + 1):
    # print(f"{d}桁")
    # 一旦1桁は無視
    # min_list = list(range(d - 1, -1, -1))
    # print(min_list)

    combinations_list = list(combinations(usable_digits, d))
    int_list = []
    for c in combinations_list:
        # print(c)
        if c[::-1][0] == 0:
            continue
        int_list.append(int("".join(map(str, c[::-1]))))
    int_list.sort()
    # print(int_list)
    for i in int_list:
        if res == k:
            print(i)
            exit()
        res += 1
