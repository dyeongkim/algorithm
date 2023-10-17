# 백준 17626 - Four Squares
import sys

input = sys.stdin.readline
N = int(input())
dp = [0,1]

for i in range(2, N+1):
    minnum = 50001
    j = 1

    while (j**2) <= i:
        minnum = min(minnum, dp[i-(j**2)])
        j += 1
    
    dp.append(minnum+1)

print(dp[N])