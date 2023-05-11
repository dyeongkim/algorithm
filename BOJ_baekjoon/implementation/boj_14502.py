# 백준 14502 - 연구소
import sys
from collections import deque

def bfs(x,y,temp_graph):
    queue = deque()
    queue.append((x,y))
    while queue :
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >= N  or ny < 0  or ny >= M:
                continue
            if temp_graph[nx][ny] != 0:
                continue
            temp_graph[nx][ny] = 2
            queue.append((nx,ny))

    
def safe_cnt(g):
    global max_safe
    s_cnt = 0
    for i in g:
        for j in i:
            if j == 0:
                s_cnt += 1
    
    if max_safe < s_cnt :
        max_safe = s_cnt

def wall(g):
    cnt = 3
    for x in range(N):
        for y in range(M):
            if g[x][y] == 0:
                g[x][y] = 1
                cnt -= 1
                if cnt == 0 :
                    return g


input = sys.stdin.readline
N, M = map(int,input().split())
dx,dy = [0,1,0,-1],[1,0,-1,0]

graph = []
v_list = []
max_safe = 0

for i in range(N):
    graph.append(list(map(int,input().split())))
    
    for j in range(M):
        if graph[i][j] == 2 :
            v_list.append((i,j))


temp_graph = graph[:]

for x,y in v_list:
    bfs(x,y,temp_graph)

safe_cnt(temp_graph)

print(max_safe)