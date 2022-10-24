N=int(input())
d_list=[int(i) for i in input().split()]
sum_heal = 0 
for i in range(N):
    for j in range(i+1, N):
        sum_heal += d_list[i]*d_list[j]
print(sum_heal)