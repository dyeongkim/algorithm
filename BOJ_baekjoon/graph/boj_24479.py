import sys
input = sys.stdin.readline
sys.setrecursionlimit(200001)
N, M, R = map(int,input().split())
graph = [[] for _ in range(N+1)]
vis = [0]*(N+1)
cnt = 0


for i in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(N):
    graph[i].sort()

def dfs(x):
    global cnt
    cnt += 1
    vis[x] = cnt
    for i in graph[x] :
        if vis[i] == 0:
            dfs(i)


dfs(R)
for i in vis[1:] :
    print(i)

