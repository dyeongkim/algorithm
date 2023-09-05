# 백준 9461 - 파도반 수열

T = int(input())

for _ in range(T):
    N = int(input())
    dp = [0] * 101

    dp[1] = 1
    dp[2] = 1
    dp[3] = 1

    for i in range(4, N+1):
        dp[i] = dp[i-2]+dp[i-3]
    
    print(dp[N])