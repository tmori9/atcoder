N, M = map(int, input().split())


def min_greater_than_x(lst, x):
    greater_than_x = [num for num in lst if num >= x]
    if len(greater_than_x) == 0:
        return -1
    else:
        return min(greater_than_x)


# 最大値でかけた場合でもMに届かない
if N * N < M:
    print(-1)
    exit()
left = N
right = M // N

# ans_list = []
ans_set = set()
for i in range(right, left + 1):
    for j in range(M // i, left + 1):
        # print(f"{i=}{j=} {i*j}")
        ans_set.add(i * j)
        if i * j >= M:
            break

print(min_greater_than_x(list(ans_set), M))
