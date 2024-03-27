# 백준 14501 - 퇴사
import sys

input = sys.stdin.readline
N = int(input())
tp = []
dp = [0] * (N + 1)
for _ in range(N):
	tp.append(list(map(int, input().split())))

for i in range(N):
	for j in range(i+tp[i][0], N+1) :
		if dp[j] < dp[i]+tp[i][1] :
			dp[j] =dp[i]+tp[i][1] 

print(dp[-1])