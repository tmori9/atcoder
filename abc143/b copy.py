from scipy.special import comb

N=int(input())
d_list=[int(i) for i in input().split()]
# comb = list(itertools.combinations(d_list, 2))
comb_list = comb(d_list, 2, exact=True)
sum_heal = 0
for i,j in comb:
    sum_heal += i*j
print(sum_heal)