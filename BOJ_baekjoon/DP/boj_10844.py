# 백준 10844 - 쉬운 계단 수

N = int(input())

dp = [[0] * 10 for _ in range(N+1)]

for i in range(1, 10):
    dp[1][i] = 1 # 길이가 1개일때는 0을 제외한 수가 계단수

for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1] # 뒷자리가 0 이면 1만 올 수 있음
        elif j == 9:
            dp[i][j] = dp[i-1][8] # 뒷자리가 9면 8만 올 수 있음
        else:
            dp[i][j] = dp[i-1][j-1]+dp[i-1][j+1] # 나머지는 뒷자리와 인접한 숫자

print(sum(dp[N]) % 1000000000)
