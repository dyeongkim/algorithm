# 백준 1018 - 체스판 다시 칠하기
import sys

input = sys.stdin.readline
N, M = map(int,input().split())
C = [input().rstrip() for _ in range(N)]

result = []

for x in range(N-7):
    for y in range(M-7):
        for a in range(2):
            cnt = 0
            for i in range(x, x+8):
                if a==0 :
                    if i % 2 == 0:
                        color = 'B'
                    else :
                        color = 'W'
                else :
                    
                    if i % 2 == 0:
                        color = 'W'
                    else :
                        color = 'B'
                
                for j in range(y, y+8):
                    if C[i][j] != color :
                        cnt +=1

                    if color == 'B' :
                        color = 'W'
                    else :
                        color = 'B'
            result.append(cnt)

print(min(result))