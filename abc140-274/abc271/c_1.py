n = int(input())
a_list = list(map(int, input().split()))
a_set = set(a_list)

amari = len(a_list) - len(a_set)
# print(f"amari: {amari}")


a_list_sort = sorted(list(a_set))
cnt = 1
pt = 0


a_list_sort.extend([10**9] * amari)
end_pt = len(a_list_sort) - 1

while True:
    if a_list_sort[pt] == cnt:
        pt += 1
        cnt += 1
    else:
        if end_pt - 1 < pt:
            break
        else:
            end_pt = end_pt - 2
            cnt += 1

    if end_pt < pt:
        break

print(cnt - 1)
