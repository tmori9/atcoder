n = int(input())
a_list = list(map(int, input().split()))
a_set = set(a_list)

amari = len(a_list) - len(a_set)
# print(f"amari: {amari}")


a_list_sort = sorted(list(a_set))
cnt = 1
pt = 0
end_pt = len(a_list_sort) - 1

while True:
    if end_pt < pt:
        if 2 <= amari:
            amari = amari - 2
            cnt += 1
            continue
        else:
            break

    if a_list_sort[pt] == cnt:
        pt += 1
        cnt += 1
        continue
    else:
        if 2 <= amari:  # 余りがあったとき
            amari = amari - 2
            cnt += 1
        else:
            end_pt = end_pt - 2
            if end_pt < pt:
                break
            cnt += 1


print(cnt - 1)
