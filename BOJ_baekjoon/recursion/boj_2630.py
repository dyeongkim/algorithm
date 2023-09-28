# 백준 2630 - 색종이 만들기
import sys

input = sys.stdin.readline
Num = int(input())
P = [list(map(int, input().split())) for _ in range(Num)]
blue = 0
white = 0

def recur(n, x, y):
    global blue, white
    color = P[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != P[i][j]:
                temp = n//2
                recur(temp, x, y)
                recur(temp, x, y+temp)
                recur(temp, x+temp, y)
                recur(temp, x+temp, y+temp)
                return
    if color == 0:
        white += 1
    else :
        blue += 1


recur(Num, 0, 0)
print(white)
print(blue)