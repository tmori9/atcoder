from itertools import groupby
N = int(input())
List = list(input())
sum_list = []
for key, value in groupby(List):
    sum_list.append(key)
print(len(sum_list))