import sys
from collections import deque
input = sys.stdin.readline

def bfs(start_x, start_y, end_x, end_y, graph) :
    queue = deque()
    queue.append((start_x, start_y))
    graph[start_x][start_y] = 0

    while queue :
        x,y = queue.popleft()
        for i in range(8):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx < 0 or ny < 0 or nx >= L or ny >= L :
                continue

            if graph[nx][ny] != -1:
                continue

            if nx == end_x and ny == end_y :
                ans.append(graph[x][y]+1)
                return

            graph[nx][ny] = graph[x][y]+1
            queue.append((nx, ny))
        
    ans.append(0)
            


T = int(input())
dx,dy = [1, 2, 2, 1, -1, -2, -2, -1],[2, 1, -1, -2, -2, -1, 1, 2]
ans = []

for i in range(T):
    L = int(input())
    graph = [[-1]*L for _ in range(L)]
    start_x, start_y = map(int,input().split())
    end_x, end_y = map(int,input().split())
    bfs(start_x, start_y, end_x, end_y, graph)


for i in ans:
    print(i)