# 백준 14503 - 로봇 청소기
#    0북 
# 3서   1동
#    2남 
#
# 0 청소안된 칸
# 1 벽

import sys

input = sys.stdin.readline

def turn() :
    r = robo[2]
    if r - 1 < 0:
        robo[2] = 3
    else :
        robo[2] = r-1
    

N,M = map(int,input().split())
robo = list(map(int,input().split()))
graph = [list(map(int,input().split())) for _ in range(N)]
dx,dy = [-1, 0, 1, 0],[0, 1, 0, -1] # 북 동 남 서

graph[robo[0]][robo[1]] = -1
result = 1



while graph[robo[0]][robo[1]] != 1 :
    chk = False
    for i in range(4):
        turn()
        nx,ny = dx[robo[2]]+robo[0], dy[robo[2]]+robo[1]

        if graph[nx][ny] == 0:
            robo[0],robo[1] = nx,ny
            graph[robo[0]][robo[1]] = -1
            result += 1
            chk = True
            break
    if not chk:
        robo[0],robo[1] = robo[0]-dx[robo[2]], robo[1]-dy[robo[2]]


print(result)