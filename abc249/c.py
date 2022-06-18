import itertools
from collections import Counter

n, k = map(int, input().split())
s_list = [input() for i in range(n)]


def check_str_sum(s_list):
    result_count = 0
    all_counter = Counter()
    for s in s_list:
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        all_counter = all_counter + Counter(d)
    dict_counter = dict(all_counter)

    for i, v in enumerate(dict_counter.values()):
        if v == k:
            result_count += 1
    return result_count


result_max = 0
for str_length in range(1, n + 1):
    combi_list = list(itertools.combinations(s_list, str_length))
    # print(combi_list)
    for one_peer in combi_list:
        # print(one_peer)
        sum_count = check_str_sum(one_peer)
        if result_max <= sum_count:
            result_max = sum_count

print(result_max)
