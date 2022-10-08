n, m = map(int, input().split())

k_list = [list(map(int, input().split())) for i in range(m)]

for i in range(n):
    check_list = [False] * n
    check_list[i] = True

    for butou in k_list:
        # print(butou[1:])
        if i + 1 in butou[1:]:
            for j in butou[1:]:
                check_list[j - 1] = True
    # print(check_list)
    if False in check_list:
        print("No")
        exit()
print("Yes")
