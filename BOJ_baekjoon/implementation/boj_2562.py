# 백준 2562 - 최댓값
import sys

input = sys.stdin.readline
num = []

for _ in range(9):
    num.append(int(input()))

M = max(num)

print(M)

for i in range(9) :
    if num[i] == M:
        print(i+1)

