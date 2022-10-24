import itertools
import math

N = int(input())
List=[list(map(int,input().split())) for i in range(N)]
roots = list(itertools.permutations(range(N)))
sum_length = 0
for root in roots:
    first_city = 100 # 存在しない
    for city in root:
        if first_city == 100:
            first_city = city
            continue
        x = List[first_city][0] - List[city][0]
        y = List[first_city][1] - List[city][1]
        sum_length += math.sqrt(pow(x,2)+pow(y,2))
print(sum_length/len(roots))