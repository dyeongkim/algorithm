# 백준 16928 - 뱀과 사다리 게임
import sys
from collections import deque

def bfs():
    while queue :
        idx = queue.popleft()
        for i in range(1, 7): # 주사위는 1~6까지
            nx = idx+i # 현재칸에서 i 만큼 갔을때 예상위치
            if nx > 100: # 100초과하면 넘기기
                continue

            if nx in snake: # 예상위치에 뱀이 있을경우 (뱀위치면 넘기려 했으나 틀렸음)
                nx = snake[nx] # 뱀위치로 변경
            elif nx in ladder : # 예상위치에 사다리가 있을경우
                nx = ladder[nx] # 사다리로 변경

            if graph[idx]+1 < graph[nx] or graph[nx] == 0: # 현재칸까지 최소거리 +1가 예상 위치의 값보다 작을때 이동해야함, 한번도 방문하지 않았을때도 이동
                graph[nx] = graph[idx]+1
                queue.append(nx)
            
        

input = sys.stdin.readline
N, M = map(int, input().split()) # 사다리수, 뱀의 수
ladder, snake = {}, {} #사다리, 맵 dict
for i in range(N): # 사다리 정보
    x, y = map(int, input().split())
    ladder[x] = y
for i in range(M): # 뱀 정보
    u, v = map(int, input().split())
    snake[u] = v
graph = [0]*101 # 해당 칸까지 최소한의 거리 저장
queue = deque()
queue.append(1) # 1번 칸에서 시작
bfs()
print(graph[100]) # 100번 칸의 최소거리 출력