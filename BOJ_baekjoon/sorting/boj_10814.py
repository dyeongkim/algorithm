# 백준 10814 - 나이순 정렬
import sys

input = sys.stdin.readline
N = int(input())
M = []
for _ in range(N):
    A, B = input().split()
    M.append((int(A), B))

M.sort(key= lambda M:M[0])

for A,B in M:
    print(A, B)    