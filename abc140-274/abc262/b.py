import numpy as np
import numpy.linalg as la

n, m = map(int, input().split())
graph = [[0] * n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1
    graph[b - 1][a - 1] = 1

A3 = la.matrix_power(graph, 3)
print(int(A3.trace() / 6))
