# 백준 18111 - 마인크래프트

import sys
input = sys.stdin.readline


N, M, B = map(int, input().split())
field = [list(map(int, input().rstrip().split())) for _ in range(N)]
ans = sys.maxsize
idx = 0

for i in range(257) :
    UB = 0
    TB = 0
    for x in range(N):
        for y in range(M):
            if field[x][y]>1:
                TB += field[x][y] - i
            else :
                UB += i - field[x][y]

    if UB > TB + B:
        continue

    cnt = TB*2 + UB

    if cnt <= ans:
        ans = cnt
        idx = i

print(ans, idx)