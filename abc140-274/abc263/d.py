N, L, R = map(int, input().split())
a_list = list(map(int, input().split()))


list_part_sum = 0
L_part_sum = 0
L_i_list = []
for i in range(0, len(a_list)):
    list_part_sum += a_list[i]
    L_part_sum += L
    # print(f"list_part_sum = {list_part_sum}")
    # print(f"L_part_sum = {L_part_sum}")
    if list_part_sum - L_part_sum > 0:
        L_i_list.append(i)

if len(L_i_list) == 0:
    L_i_list = [-1]
# print(L_i_list)

a_list_rev = a_list[::-1]
list_part_sum = 0
R_part_sum = 0
R_i_list = []
for i in range(0, len(a_list_rev)):
    list_part_sum += a_list_rev[i]
    R_part_sum += R
    # print(f"list_part_sum = {list_part_sum}")
    # print(f"R_part_sum = {R_part_sum}")
    if list_part_sum - R_part_sum > 0:
        R_i_list.append(len(a_list_rev) - i - 1)

if len(R_i_list) == 0:
    R_i_list = [len(a_list)]
# print(R_i_list)


def result_sum(l, r):
    left = L * (l + 1)
    # print(left)
    # print(a_list[l + 1 : r])
    right = R * (len(a_list) - r)
    # print(right)
    return left + sum(a_list[l + 1 : r]) + right


sum_all = []
for l_i in L_i_list:
    for r_i in R_i_list:
        if l_i + 1 >= r_i:
            continue
        sum_all.append(result_sum(l_i, r_i))

print(min(sum_all))
