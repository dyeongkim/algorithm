# 백준 10815 - 숫자 카드
import sys

input = sys.stdin.readline
N = int(input())
card_N = list(map(int, input().split()))
M = int(input())
card_M = list(map(int, input().split()))
dp = [0]*M

result_S = set(card_M)&set(card_N)

for i in range(M) :
    if card_M[i] in result_S:
        dp[i] = 1

print(" ".join(map(str,dp)))
