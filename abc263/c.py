n, m = map(int, input().split())

import itertools

l = list(range(1, m + 1))
for v in itertools.combinations(l, n):
    print(*list(v))
