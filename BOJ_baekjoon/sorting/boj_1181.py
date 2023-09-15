# 백준 1181 - 단어 정렬
import sys

input = sys.stdin.readline
N = int(input())
S = []

for _ in range(N):
    temp = input().rstrip()
    if not [len(temp), temp] in S :
        S.append([len(temp), temp])
S.sort()

for x, y in S :
    print(y)