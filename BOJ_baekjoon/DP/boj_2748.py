# 백준 2748 - 피보나치 수 2

n = int(input())
dp = [0] * (n  + 1)
dp[0] = 0
dp[1] = 1

def fibo(n):
	if dp[n] != 0 :
		return dp[n]
	for i in range(2, n+1) :
		dp[i] = dp[i-1]+dp[i-2]	
	return dp[n]

print(fibo(n))	