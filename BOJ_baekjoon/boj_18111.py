# 백준 18111 - 마인크래프트
import sys

input = sys.stdin.readline
N, M, B = map(int,input().split())
ground = []

for _ in range(N):
    ground.append(list(map(int, input().split())))

for i in range(257):
    for j in range(N):
        for k in range(K):
            