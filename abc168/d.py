import numpy as np
from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson

N, M = map(int, input().split())
target_root = [list(map(int, input().split())) for i in range(M)]

print(target_root)

m =[ [0]*N for i in range(N)]
for path in target_root:
    m[path[0]-1][path[1]-1] = 1
m_np = np.array(m)
a = m_np+m_np.T
print(a)
shortest_path_list = shortest_path(a, indices=0).tolist()
print(shortest_path_list[1:])
result_root = [0]*(N-1)
if 0.0 in shortest_path_list[1:]:
    print("No")
else:
    
    