# 백준 14500 - 테크로미노
import sys
from collections import deque

def bfs():
    

input = sys.stdin.readline
N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
