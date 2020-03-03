import sys
input = sys.stdin.readline
 
n,m,k = map(int,input().split())
graph = {i+1:[] for i in range(n)}
block = {i+1:[] for i in range(n)}
ans = [-1 for _ in range(n)]
 
for _ in range(m):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)
for _ in range(k):
  c,d = map(int,input().split())
  block[c].append(d)
  block[d].append(c)

print(graph)
print(block)