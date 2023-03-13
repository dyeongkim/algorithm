import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y, color):
    queue = deque()
    vis[x][y] = True
    queue.append((x,y))
    while queue :
        x,y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            
            if vis[nx][ny] == True:
                continue

            if graph[nx][ny] == color :
                vis[nx][ny] = True
                queue.append((nx,ny))

N = int(input())
graph = []
vis = [[False]*N for _ in range(N)]
dx, dy = [-1,0,1,0],[0,1,0,-1]
cnt, cnt_RG = 0, 0
for i in range(N):
    graph.append(list(input().strip()))

for i in range(N):
    for j in range(N):
        if vis[i][j] == False :
            bfs(i,j, graph[i][j])
            cnt += 1
            


vis = [[False]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if graph[i][j] == "G" :
            graph[i][j] = "R"

for i in range(N):
    for j in range(N):
        if vis[i][j] == False :
            bfs(i,j, graph[i][j])
            cnt_RG += 1
print(cnt, cnt_RG)
