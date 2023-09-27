# 백준 2630 - 색종이 만들기
import sys

input = sys.stdin.readline
N = int(input())
P = [list(map(int, input().split())) for _ in range(N)]

def recur(n, x, y):
    if(n == 1):
        return P[x][y]
    
    recur(x,y)
    recur(x,y+1)
    recur(x+1,y)
    recur(x+1,y+1)