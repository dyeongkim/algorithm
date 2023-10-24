# 백준 2738 - 행렬 덧셈
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
A = []
B = []
result = []
for i in range(N):
    A.append(list(map(int, input().split())))
for i in range(N):
    B.append(list(map(int, input().split())))

for i in range(N):
    temp = []
    for j in range(M):
        temp.append(A[i][j] + B[i][j])
    result.append(temp)

for i in range(N):
    for j in range(M):
        print(result[i][j], end=" ")
    print()