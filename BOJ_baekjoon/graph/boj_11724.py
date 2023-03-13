import sys
from collections import deque
input = sys.stdin.readline

def add_node(x,y) :
    graph[x] += [y]
    graph[y] += [x]

def bfs(start):
    queue = deque()
    vis.append(start)
    queue.append(start)
    while queue:
        u = queue.popleft()
        for i in graph[u]:
            if i not in vis:
                vis.append(i)
                queue.append(i)

    res.append(1)

N,M = map(int, input().split())

graph = [[] for i in range(N)]
vis = []
res = []
for i in range(M):
    x,y = map(int, input().split())
    add_node(x-1, y-1)

for i in range(N):
    if i not in vis:
        bfs(i)

print(len(res))