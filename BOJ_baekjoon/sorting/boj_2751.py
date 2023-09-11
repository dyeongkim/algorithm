# 백준 2751 - 수 정렬하기 2
import sys

input = sys.stdin.readline
N = int(input())
s = []

for _ in range(N):
    s.append(int(input()))

s.sort()

for i in s:
    print(i)