n = int(input())
A_list = list(map(int, input().split()))

result_list = []
A_set = set(A_list)
max_list = sorted(list(A_set), reverse=True)


for i, max_value in enumerate(max_list):
    same_count = 0
    check_list = []
    for j, value in enumerate(A_list):
        if value == max_value:
            same_count += 1
            if not(i == len(max_list)-1):
                A_list[j] = max_list[i+1]
        else:
            if same_count >= 1:
                check_list.append(same_count)
            same_count = 0
    if same_count >= 1:
        check_list.append(same_count)
    result_list.append(max(check_list)*max_value)

print(max(result_list))
