from collections import deque

n = int(input())
x_list = [list(map(int, input().split())) for i in range(n)]

all_q = deque()

while True:
    if all_list == []:
        for i in range(2, n+1):
            all_q.append([1,i])
    else: # 2回目以降
        for i in len(all_q):
            target_list = all_q.pop(0)



print(all_list)