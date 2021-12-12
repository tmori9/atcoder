# 深さ優先探索
from collections import deque
import itertools
import collections

n, m = map(int, input().split())

if m == 0:
    print("Yes")
    exit()

U = []
V = []
x = []
for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    x.append(u)
    x.append(v)
    U.append(u)
    V.append(v)

# 閉路を持たない木
ans = 0
# 探索済み頂点リスト
Visited = [0] * n

# 頂点iからdfs 探索済み頂点リストを更新していき 探索済み頂点をpopしたら閉路
def dfs(i):
    que = deque()
    que.append(i)  # 探索をはじめる頂点をpush
    flag = True  # 閉路判別フラグ Trueで閉路なし

    # queが空になるまで探索
    while len(que) != 0:
        k = que.pop()  # 探索する頂点kをpop
        if Visited[k] != 0:
            flag = False
            print("No")
            exit()
        else:
            Visited[k] = 1  # 頂点kの探索済みリストを更新
            for j in range(m):
                # 未探索の頂点ならpush
                if U[j] == k and Visited[V[j]] == 0:
                    que.append(V[j])
                elif V[j] == k and Visited[U[j]] == 0:
                    que.append(U[j])

    # 頂点iからの探索を終えたとき閉路があるかを返す
    return flag


# すべての頂点で未探索ならdfs
for l in range(n):
    if Visited[l] == 0:
        if dfs(l):  # 探索して閉路がなければans+1
            ans += 1

c = collections.Counter(x)
common_list = c.most_common()
if c.most_common()[0][1] >= 3:
    print("No")
else:
    print("Yes")