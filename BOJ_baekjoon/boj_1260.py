from collections import deque
import sys

    
def add_edge(a, b):
    graph[a][b] = True
    graph[b][a] = True


def dfs(start, vis=set()):
    vis.add(start)
    print(start, end=' ')
    for n in range(N+1):
        if n not in vis and graph[start][n]:
            dfs(n,vis)

def bfs(start, vis=set()):
    queue = deque()
    queue.append(start)
    while queue:
        start = queue.popleft()
        print(start, end=' ')
        vis.add(start)
        for n in range(N+1):
            if n not in vis and graph[start][n]:
                vis.add(n)
                queue.append(n)


input = sys.stdin.readline
N, M, V = map(int,input().split())
graph = [[False]*(N+1) for _ in range(N+1)]

for i in range(M):
    a,b = map(int,input().split())
    add_edge(a, b)

dfs(V)
print()
bfs(V)