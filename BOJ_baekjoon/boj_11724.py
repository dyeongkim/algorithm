import sys
from collections import deque
input = sys.stdin.readline

def add_node(u, v):
    graph[u] += [v]
    graph[v] += [u]

def bfs(x, y):
    queue = deque()
    graph[x][y] = 0
    queue.append((x,y))
    while queue:
        

N,M = map(int, input().split())

graph = [[0]*N for _ in range(N)]

for i in range(M):
    x,y = map(int, input().split())
    add_node(x, y)