from collections import deque
from math import factorial

def combinations_count(n, r):
    ''' 組み合わせ '''
    return factorial(n) // (factorial(n - r) * factorial(r))

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
        if list_que[0] + list_que[-1] > Max_value:
            sum_value += combinations_count(len(list_que), 2)
            break
        else:
            list_que.pop()
print(sum_value)