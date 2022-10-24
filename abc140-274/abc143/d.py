from collections import deque
from itertools import islice

N = int(input())
List=list(map(int,input().split()))
List.sort(reverse=True)
flag = True
while flag:
    if len(List) <= 2:
        print(0)
        exit()
    if List[0] > List[1]+List[2]:
        List = List[1:]
    else:
        flag = False
list_que = deque(List)
sum_value = 0
while len(list_que) >= 3:
    Max_value = list_que.popleft()
    while len(list_que) >= 2 and int(list_que[0]) > Max_value/2:
        for i,v in enumerate(list_que):
            for v2 in list(islice(list_que,i+1,len(list_que))):
                if Max_value < v + v2:
                    sum_value += 1
                else:
                    break
        list_que.popleft()
print(sum_value)