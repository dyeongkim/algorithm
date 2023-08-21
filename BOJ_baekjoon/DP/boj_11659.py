#백준 11659 - 구간 합 구하기 4
import sys
input = sys.stdin.readline

N, M = map(int,input().split())

num = list(map(int, input().split()))
dp = [0]
tmp = 0
for i in num:
    tmp += i
    dp.append(tmp)
    
for _ in range(M) :
    result = 0
    i, j = map(int, input().split())
    print(dp[j]-dp[i-1])