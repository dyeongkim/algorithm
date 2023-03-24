import sys
from collections import deque
input = sys.stdin.readline

def bfs(start) :
    global cnt
    queue = deque()
    ans[start] = cnt
    vis[start] = True
    
    queue.append(start)

    while queue:
        x = queue.popleft()
        graph[x].sort(reverse=True)
        
        for i in graph[x]:
            if not vis[i] :
                cnt += 1
                vis[i] = True
                ans[i] = cnt
                queue.append(i)
            



N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
ans = [0]*(N+1)
vis = [False]*(N+1)
cnt = 1


for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

bfs(R)

for i in ans[1:]:
    print(i)