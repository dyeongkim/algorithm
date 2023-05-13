# 백준 14502 - 연구소
import sys
import copy
from collections import deque

# 바이러스 퍼지는 함수
def bfs():
    queue = deque()
    for x,y in v_list:
        queue.append((x,y))
    temp_graph = copy.deepcopy(graph)
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
    safe_cnt(temp_graph)

# 안전구역 세는 함수
def safe_cnt(temp_graph):
    global max_safe
    s_cnt = 0
    for i in temp_graph:
        for j in i:
            if j == 0:
                s_cnt += 1
    
    if max_safe < s_cnt :
        max_safe = s_cnt

# 벽 세우는 함수
def wall(start, count):
    if count == 3: # 3개가 다 세워졌으면 BFS로 바이러스 퍼트리기
        bfs()
        return
    for i in range(start, len(empty_list)):
        x,y = empty_list[i]
        if graph[x][y] == 0: # 빈공간 만나면 벽 세우기
            graph[x][y] = 1 
            wall(i+1, count+1) # 현재 벽 개수 추가해서 재귀
            graph[x][y] = 0 # 다시 벽 초기화


input = sys.stdin.readline
N, M = map(int,input().split())
dx,dy = [0,1,0,-1],[1,0,-1,0]

graph = [] # 연구소 지도
v_list = [] # 바이러스 위치 리스트
empty_list = [] # 빈공간 위치 리스트
max_safe = 0

for i in range(N): # 지도 입력받기
    graph.append(list(map(int,input().split())))
    
    for j in range(M):
        if graph[i][j] == 2 : # 바이러스 위치 저장
            v_list.append((i,j))
        elif graph[i][j] == 0 : # 빈공간 위치 저장
            empty_list.append((i,j))

wall(0, 0) # 벽세우기 시작

print(max_safe)