# 백준 18111 - 마인크래프트

import sys
input = sys.stdin.readline


N, M, B = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]
ans = sys.maxsize
idx = 