# 백준 1149 - RGB거리


N = int(input())
dp = [[0]*3 for i in range(N+1)]
h = [0] * (N+1) 
for i in range(1,N+1):
    h[i] = list(map(int,input().split()))

dp[1][0] = h[1][0]
dp[1][1] = h[1][1]
dp[1][2] = h[1][2]

for i in range(2, N+1):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + h[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + h[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + h[i][2]

print(min(dp[i]))