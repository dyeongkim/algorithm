# 백준 10989 - 수 정렬하기 3
import sys

input = sys.stdin.readline
N = int(input())
num = [0] * 100001
for i in range(N):
    num[int(input())] += 1

for i in range(len(num)):
    if num[i] > 0:
        for j in range(num[i]):
            print(i)
