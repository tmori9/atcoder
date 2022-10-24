N,M=map(int,input().split())
sc_list=[list(map(int,input().split())) for i in range(M)]

result_n = [0] * N

flag_lsit = [False] * N

for line in sc_list:
    first_n = line[0]
    second_n = line[1]

    if flag_lsit[first_n-1] == False:
        result_n[first_n-1] = second_n
        flag_lsit[first_n-1] = True
    else:
        if not(result_n[first_n-1] == second_n):
            print(-1)
            exit()
            
# 先頭が0
if result_n[0] == 0:
    if N == 1:
        print(0)
        exit()
    if flag_lsit[0] == True: # 変更があった
        print(-1)
    else:
        result_n[0] = 1
        for i in result_n:
            print(i,end="")
        print()

else:
    for i in result_n:
        print(i,end="")
    print()
