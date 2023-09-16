# 백준 2798 - 블랙잭
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
card = list(map(int, input().split()))
l = len(card)
result = -1

for i in range(0, l-2) :
    for j in range(i+1, l-1):
        for k in range(j+1, l):
            if card[i]+card[j]+card[k] <= M:
                result = max(result, card[i]+card[j]+card[k])
                

print(result)