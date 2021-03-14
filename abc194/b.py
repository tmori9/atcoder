n = int(input())
task_list = [list(map(int, input().split())) for i in range(n)]

all_list = []
for i, time in enumerate(task_list):
    for j in range(len(task_list)):
        if i == j:
            all_list.append(task_list[i][0]+task_list[i][1])
        else:
            all_list.append(max(task_list[i][0], task_list[j][1]))

print(min(all_list))
