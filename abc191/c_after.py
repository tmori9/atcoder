h, w = map(int, input().split())

s_list = []
for line in range(h):
    one_list = list(input())
    s_list.append(one_list)

result_sum = 0
for i, line in enumerate(s_list):
    if i == len(s_list)-1:
        continue
    for j, pt in enumerate(line):
        if j == len(line)-1:
            continue
        check = 0
        if s_list[i][j] == '#':
            check += 1
        if s_list[i+1][j] == '#':
            check += 1
        if s_list[i][j+1] == '#':
            check += 1
        if s_list[i+1][j+1] == '#':
            check += 1

        if check == 1 or check == 3:
            result_sum += 1

print(result_sum)
