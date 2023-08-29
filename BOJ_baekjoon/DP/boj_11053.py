# 백준 11053 - 가장 긴 증가하는 부분 수열

N = int(input())
dp = [0] * (N)
num = list(map(int,input().split()))

for i in range(N) :
    for j in range(i):
        if num[i] > num[j] and dp[i] < dp[j] :
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))