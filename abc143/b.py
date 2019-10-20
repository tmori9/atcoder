import itertools
N=int(input())
d_list=[int(i) for i in input().split()]
comb = list(itertools.combinations(d_list, 2))
sum_heal = 0
for i,j in comb:
    sum_heal += i*j
print(sum_heal)