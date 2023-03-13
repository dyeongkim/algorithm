import sys
from collections import deque
input = sys.stdin.readline

T = int(input())


def bfs(x,y) : 
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if graph[nx][ny] != 0 :
                graph[nx][ny] = 0
                queue.append((nx,ny))

    res.append(1)


for x in range(T):
    M, N, K = map(int, input().split())

    graph = [[0]*(M) for _ in range(N)]

    dx, dy = [1,0,-1,0],[0,1,0,-1]

    res = []

    for i in range(K):
        x,y = map(int, input().split())
        graph[y][x] = 1

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                bfs(i,j)
    
    print(len(res))

