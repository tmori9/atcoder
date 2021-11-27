from collections import deque

n = int(input())
target_str = list(input())
q = int(input())
query_list = [list(map(int, input().split())) for i in range(q)]
result_list = list(range(1, n * 2 + 1))

for i_command in query_list:
    if i_command[0] == 2:
        tmp = target_str[0:n]
        target_str = target_str[n:] + tmp

    elif i_command[0] == 1:
        target_str[i_command[1] - 1], target_str[i_command[2] - 1] = (
            target_str[i_command[2] - 1],
            target_str[i_command[1] - 1],
        )

print(*target_str, sep="")

print(*target_str, sep="")