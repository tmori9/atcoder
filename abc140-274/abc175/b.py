import itertools

N = int(input())
L_list = list(map(int, input().split()))

list_comb = list(itertools.combinations(L_list, 3))

result_sum = 0
for i in list_comb:
    if i[0] == i[1] or i[1] == i[2] or i[2] == i[0]:
        continue
    if i[0]+i[1]>i[2] and i[1]+i[2]>i[0] and i[2]+i[0]>i[1]:
        result_sum += 1
print(result_sum)