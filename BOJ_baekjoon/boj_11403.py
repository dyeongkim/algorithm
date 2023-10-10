# 백준 11403 - 경로 찾기
import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
queue = deque()

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            queue.append(i,j)