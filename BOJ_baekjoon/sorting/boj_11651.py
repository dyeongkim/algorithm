# 백준 11651 - 좌표 정렬하기 2

import sys
input = sys.stdin.readline
N = int(input())
M = []
for _ in range(N):
    x, y = map(int, input().split())
    M.append((y,x))

M.sort()

for y, x in M :
    print(x, y)