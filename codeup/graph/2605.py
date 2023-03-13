import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y, color):
    graph[x][y] = 0

    queue = deque()
    queue.append((x,y))

    cnt = 1

    while queue :
        x,y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx < 0 or nx >= 7 or ny < 0 or ny >= 7:
                continue
            
            if graph[nx][ny] != color:
                continue

            graph[nx][ny] = 0
            queue.append((nx,ny))
            cnt += 1
    
    if cnt >= 3:
        res.append(1)

graph = []
res = []
dx, dy = [-1,0,1,0],[0,1,0,-1]
for i in range(7):
    graph.append(list(map(int,input().split())))

for i in range(7):
    for j in range(7):
        if graph[i][j] != 0:
            bfs(i,j,graph[i][j])

print(len(res))