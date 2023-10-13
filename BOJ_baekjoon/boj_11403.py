# 백준 11403 - 경로 찾기
import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
graph = [list(input().split()) for _ in range(N)]
queue = deque()

for k in range(N) :
    for i in range(N):
        for j in range(N):
            if graph[i][j] == "1" or (graph[i][k] == "1" and graph[k][j] == "1"):
                    graph[i][j] ="1"

for i in range(N):
     print(" ".join(graph[i]))