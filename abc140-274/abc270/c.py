N, X, Y = map(int, input().split())
uv = [list(map(int, input().split())) for _ in range(N - 1)]

g = [[] for _ in range(N + 1)]

for u, v in uv:
    g[u].append(v)
    g[v].append(u)

seen = [False] * (N + 1)
ans = []

# print(g)


def dfs(a):
    ans.append(a)

    if a == Y:
        print(*ans)
        exit()

    seen[a] = True

    for v in g[a]:
        if seen[v]:
            continue
        dfs(v)
        ans.pop()


dfs(X)
