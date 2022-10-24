n = int(input())
a_list = list(map(int, input().split()))

a_list_sorted = sorted(a_list)

j = 0
remove_flag = False
while True:
    remove_flag = False
    if j >= len(a_list_sorted):
        break
    check = a_list_sorted[j]
    i = j-1 # 検索の初期値
    while True:
        i += 1
        if i >= len(a_list_sorted):
            break
        value = a_list_sorted[i]
        if j >= i:
            continue
        if value == check: # 同じ数字を持つ
            remove_flag = True
        if value % check == 0:
            del a_list_sorted[i]
            i -= 1
    if remove_flag:
        del a_list_sorted[j] # 探索した数字
        j -= 1
    j += 1

print(len(a_list_sorted))
