import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

print(graph)