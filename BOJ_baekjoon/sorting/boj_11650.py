# 백준 11650 - 좌표 정렬하기

import sys
input = sys.stdin.readline
N = int(input())
M = []
for _ in range(N):
    M.append(list(map(int, input().split())))

M.sort()
for x,y in M :
    print(x, y)