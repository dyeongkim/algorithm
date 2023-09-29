# 백준 14940 - 쉬운 최단거리
import sys
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
result = [[0]*m for _ in range(n)]
dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]
queue = deque()

for i in range(n):
    for j in range(m) :
        if graph[i][j] == 2:
            queue.append((i, j))


def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 > nx or nx >= n or 0 > ny or ny >= m :
                continue
            

            if result[nx][ny] == 0 and graph[nx][ny] == 1:
                result[nx][ny] = result[x][y]+1
                queue.append((nx,ny))


bfs()

for i in range(n):
    for j in range(m) :
        if graph[i][j] == 1 and result[i][j] == 0:
            result[i][j] = -1

for i in range(n):
    print(' '.join(map(str,result[i])))