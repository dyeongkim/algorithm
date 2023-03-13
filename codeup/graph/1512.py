import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [[0] * N for _ in range(N)]


dx, dy = [-1,0,1,0],[0,1,0,-1]


def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 1

    while queue :
        x,y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if graph[nx][ny] != 0:
                continue

            graph[nx][ny] = graph[x][y] + 1
            queue.append((nx,ny))

x,y = map(int, input().split())

bfs(x-1,y-1)

for i in range(N):
    for j in range(N):
        print(graph[i][j], end=' ')
    print()