from collections import deque

n = int(input())
target_str = input()
q = int(input())
query_list = [list(map(int, input().split())) for i in range(q)]


target_que = deque(target_str)
"""
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
"""
for i_command in query_list:
    if i_command[0] == 2:
        for i in range(n):
            target_que.append(target_que.popleft())

    elif i_command[0] == 1:
        tmp = target_que[i_command[2] - 1]
        target_que[i_command[2] - 1] = target_que[i_command[1] - 1]
        target_que[i_command[1] - 1] = tmp
print(*target_que, sep="")