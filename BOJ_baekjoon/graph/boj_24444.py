import sys
from collections import deque

def bfs(start) :
    global cnt
    queue = deque()
    
    vis[start] = cnt
    queue.append(start)

    while queue:
        x = queue.popleft()
        
        for i in graph[x]:
            if not vis[i] :
                cnt += 1
                queue.append(i)
            



N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
vis = [0]*(N+1)
cnt = 1


for i in range(M):
    u, v = map(int, input().split())

for i in graph :
    i.sort()

bfs(R)

for i in vis[1:]:
    print(i)