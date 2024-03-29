# 백준 2133 - 타일 채우기

N = int(input())
dp = [0] * 31

dp[2] = 3

for i in range(4,N+1):
    if i % 2 == 1 :
        continue
    dp[i] = dp[i-2] * dp[2]
    for j in range(i - 4, -1, -2):
        dp[i] += dp[j]*2

    dp[i] += 2

print(dp[N])