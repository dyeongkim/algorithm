# 백준 11055 - 가장 큰 증가하는 부분 수열

N = int(input())
num = list(map(int,input().split()))
dp = [0] * (N)


for i in range(N):
    for j in range(i):
        if num[i] > num[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += num[i]

print(max(dp))