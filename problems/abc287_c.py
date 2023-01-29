from collections import defaultdict


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return "\n".join(f"{r}: {m}" for r, m in self.all_group_members().items())


n, m = map(int, input().split())
graph = [[] for _ in range(n)]

uf = UnionFind(n)

one_num = 0  # 次数1のカウント
two_num = 0  # 次数2のカウント

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1

    graph[a].append(b)
    graph[b].append(a)

    uf.union(a, b)

for one in graph:
    if len(one) == 1:
        one_num += 1
    elif len(one) == 2:
        two_num += 1
    else:
        print("No")
        exit()

if one_num == 2 and uf.group_count() == 1:
    print("Yes")
else:
    print("No")
