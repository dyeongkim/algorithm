# 백준 21736 - 헌내기는 친구가 필요해
import sys
from collections import deque

input = sys.stdin. readline
N, M = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(N)]
queue = deque()
dx, dy = [-1, 0, 1, 0],[0, 1, 0, -1]

for i in range(N):
    for j in range(M):
        if graph[i][j] == "I":
            queue.append((i,j))

def bfs():
    cnt = 0
    while queue :
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if nx >= N or ny >= M or nx < 0 or ny < 0 :
                continue
            
            if graph[nx][ny] == "X":
                continue
            elif graph[nx][ny] == "P":
                cnt += 1

            queue.append((nx,ny))
            graph[nx][ny] = "X"
    
    return cnt

result = bfs()

if result == 0:
    print("TT")
else : 
    print(result)