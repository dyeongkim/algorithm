import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y, color):
    queue = deque()
    graph[x][y] = 0
    queue.append((x,y))
    while queue :
        x,y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            
            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == color :
                graph[nx][ny] = 0
                queue.append((nx,ny))
    res.append(1)

def bfs_RG(x,y, color):
    queue = deque()
    graph[x][y] = 0
    queue.append((x,y))
    while queue :
        x,y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            
            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == color :
                graph[nx][ny] = 0
                queue.append((nx,ny))
    res.append(1)


N = int(input())
graph = []
dx, dy = [-1,0,1,0],[0,1,0,-1]
res = []
res_RG = []
for i in range(N):
    graph.append(list(input().strip()))

for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            bfs(i,j, graph[i][j])

print(len(res), end= ' ')
print(len(res_RG))
