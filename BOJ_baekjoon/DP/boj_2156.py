# 백준 2156 - 포도주 시식
'''
n = int(input())
s = [0] * (n+1)
dp = [0] * (n+1)
tot = 0
for i in range(1,n+1):
    temp = int(input())
    s[i] = temp
    tot += temp

if n <= 2 :
    print(tot)
    exit()

dp[1] = s[1]
dp[2] = s[2]
dp[3] = s[3]
for i in range(4, n+1):
    dp[i] = min(dp[i-2], dp[i-3], dp[i-1]) + s[i]

print(tot-min(dp[n-2],dp[n-1],dp[n]))
'''

