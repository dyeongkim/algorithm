# 백준 2563 - 색종이
import sys

input = sys.stdin.readline

result = [[0] * 101  for _ in range(101)]

N = int(input())
for _ in range(N):
    x, y = map(int,input().split())

    for i in range(x, x+10) :
        for j in range(y, y+10):
            result[i][j] = 1
s = 0
for _ in result:
    s += sum(_)
print(s)