# 백준 15686 - 치킨 배달
import sys
import copy
from collections import deque

def c_make(st, count):
    if count == M:
        g = copy.deepcopy(temp_graph)
        print(g)
        bfs(g)
        return
    for i in range(st, len(c_list)):
        x,y = c_list[i]
        graph[x][y] = -1
        c_make(i+1, count+1)
        graph[x][y] = 0


def bfs(g):
    global result
    while queue:
        h_queue = deque()
        h_queue.append(queue.popleft())
        while h_queue :
            x,y = h_queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= N or ny < 0 or ny >= N :
                    continue
                if g[nx][ny] != 0 or graph[nx][ny] == 1:
                    continue
                if graph[nx][ny] == -1 :
                    result += g[x][y] + 1
                    break
                g[nx][ny] += g[x][y] + 1
                queue.append((nx,ny))
    # c_cnt(temp_graph)
    

'''
def c_cnt(g):
    global result
    temp = 0
    for x,y in temp_c_list:
        temp += g[x][y]
    if result > temp :
        result = temp
'''

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
temp_graph = [[0]*N for _ in range(N)]
queue = deque()
c_list = []
temp_c_list = []
result = 0

dx, dy = [0, -1, 0, 1],[-1, 0, 1, 0]

for i in range(N) :
    for j in range(N) :
        if graph[i][j] == 2 :
            c_list.append((i,j))  
        elif graph[i][j] == 1 :
            queue.append((i,j))
            
c_make(0,0)
print(result)

