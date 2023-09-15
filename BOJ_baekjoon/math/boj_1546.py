# 백준 1546 - 평균
import sys

input = sys.stdin.readline

N = int(input())
score = list(map(int, input().split()))
M = max(score)

for i in range(N):
    score[i] = score[i]/M

print(sum(score)/N*100)