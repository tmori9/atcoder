N, Q = map(int, input().split())
query_list = [list(map(int, input().split())) for i in range(N)]
ans_list = [list(map(int, input().split())) for i in range(Q)]

for i, j in ans_list:
    print(query_list[i - 1][j])
