# 백준 11052 - 카드 구매하기

N = int(input())
P = [0] + list(map(int,input().split()))
dp = [0] * (N+1)

for i in range(1, N+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j] + P[j])

print(dp[i])