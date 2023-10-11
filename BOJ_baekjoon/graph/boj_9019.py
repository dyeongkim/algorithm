# 백준 9019 - DSLR
import sys
from collections import deque

def bfs(A, B):
    queue = deque([A])
    vis = [False] * 10000
    vis[A] = True
    graph = [""] * 10000

    while queue:
        idx = queue.popleft()
        if idx == B:
            return graph[idx]

        nidx = (idx * 2) % 10000
        if not vis[nidx]:
            graph[nidx] = graph[idx] + "D"
            vis[nidx] = True
            queue.append(nidx)

        nidx = 9999 if idx == 0 else idx - 1
        if not vis[nidx]:
            graph[nidx] = graph[idx] + "S"
            vis[nidx] = True
            queue.append(nidx)

        nidx = (idx % 1000) * 10 + idx // 1000
        if not vis[nidx]:
            graph[nidx] = graph[idx] + "L"
            vis[nidx] = True
            queue.append(nidx)

        nidx = (idx % 10) * 1000 + idx // 10
        if not vis[nidx]:
            graph[nidx] = graph[idx] + "R"
            vis[nidx] = True
            queue.append(nidx)

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    print(bfs(A, B))
