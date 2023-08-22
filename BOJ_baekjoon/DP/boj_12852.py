# 백준 12852 - 1로 만들기 2

N = int(input())
dp = [0] * (N+1)
ans = [0] * (N+1)

for i in range(2, N+1) :
    dp[i] = dp[i-1] + 1
    ans[i] = i-1

    if i%2 == 0 and dp[i//2]+1 < dp[i] :
        dp[i] = dp[i//2]+1
        ans[i] = i//2

    if i%3 == 0 and dp[i//3]+1 < dp[i] :
        dp[i] = dp[i//3]+1
        ans[i] = i//3

print(dp[N])
while (N>=1):
    print(N, end="")
    if N == 1 : 
        break
    print(" ",end="")
    N = ans[N]