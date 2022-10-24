N = int(input())
A_list = list(map(int,input().split()))
result_list = [0]*N
for i, val in enumerate(A_list):
    result_list[val-1] = i+1
print(*result_list)
