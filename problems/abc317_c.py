n, m = map(int, input().split())

graph = [[0] * (n) for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a - 1][b - 1] = c
    graph[b - 1][a - 1] = c

ans = 0
passed = [False] * n  # 通った道を記録する


def dfs(v, cost):  # vが現在地点, costが現在のコスト
    global ans
    passed[v] = True
    if cost > ans:  # 最大コストだったら回答を更新
        ans = cost
    for i in range(n):
        if not passed[i] and graph[v][i] != 0:
            dfs(i, cost + graph[v][i])
    passed[v] = False


for i in range(n):
    dfs(i, 0)

print(ans)
