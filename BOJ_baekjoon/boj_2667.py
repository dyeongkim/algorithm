import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = []
res = []
dx, dy = [-1,0,1,0],[0,-1,0,1]
for i in range(N):
    graph.append(list(map(int,input().strip())))

def bfs(x, y):
    queue = deque()
    graph[x][y] = -1
    queue.append((x,y))
    cnt = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if graph[nx][ny] != -1 and graph[nx][ny] != 0:
                graph[nx][ny] = -1
                queue.append((nx,ny))
                cnt += 1
    res.append(cnt)



for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            bfs(i,j)

res.sort()

print(len(res))
for i in res :
    print(i)