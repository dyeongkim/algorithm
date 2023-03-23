import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
N, M, R = map(int,input().split())
graph = [[] for _ in range(N+1)]
vis = [False] * (N+1)
ans = [0] * (N+1)
cnt = 1


for i in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in graph:
    i.sort(reverse=True)

def dfs(x):
    global cnt
    vis[x] = True
    ans[x] = cnt
    for i in graph[x] :
        if not vis[i]:
            cnt += 1
            dfs(i)


dfs(R)
for i in ans[1:] :
    print(i)

