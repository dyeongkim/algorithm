# 백준 2167 - 2차원 배열의 합

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
li = []

for i in range(N):
    li.append(list(map(int,input().split())))

K = int(input())

for _ in range(K):
    i,j,x,y = map(int,input().split())
    nx, ny = i-1, j-1
    result = 0
    while True :
        
        result += li[nx][ny]

        ny += 1
        if ny >= M :
            ny = 0
            nx += 1
        
        if nx >= x or ny >= y :
            print(result)
            break

        
        
            
