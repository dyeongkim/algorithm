import sys
from collections import deque
input = sys.stdin.readline

def bfs(z, y, x) :
    queue = deque()
    queue.append((z,y,x))

    while queue :
        z, y, x = queue.popleft()

        for i in range(6):
            nx = dx[i]+x
            ny = dy[i]+y
            nz = dz[i]+z

            if nx < 0 or ny < 0 or nz < 0 or nx >= M or ny >= N or nz >= H:
                continue

            if graph[nz][ny][nx] != 0 :
                continue
            
            graph[nz][ny][nx] = graph[z][y][x] + 1 
            queue.append((nz,ny,nx))



M, N, H = map(int, input().split())
dx, dy, dz =[1, 0, -1, 0, 0, 0],[0, 1, 0, -1, 0, 0],[0, 0, 0, 0, 1, -1]
graph = []

for i in range(H):
    temp = []
    for j in range(N):
        temp.append(list(map(int,input().split())))
    graph.append(temp)

for z in range(H):
    for y in range(N):
        for x in range(M):
            if graph[z][y][x] == 1 :
                bfs(z,y,x)

result = []

for z in range(H):
    for y in range(N):
        for x in y:
            if x == 0 :
                print(-1)
                exit(0)
    