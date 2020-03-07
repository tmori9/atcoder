import re
N,P=map(int,input().split())
S = input()

check_list = []

max_n = int(S)//P
result = 0

for i in range(1, max_n+1):
    result += S.count(str(i*P))

print(result)
