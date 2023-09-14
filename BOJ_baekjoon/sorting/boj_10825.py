# 백준 10825 - 국영수
import sys

input = sys.stdin.readline
N = int(input())
M = []
for _ in range(N) :
    A, B, C, D = input().split()
    M.append((A, int(B), int(C), int(D)))
    
M.sort(key= lambda M : (-M[1], M[2], -M[3], M[0]))

for i in range(N):
    print(M[i][0])