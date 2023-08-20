# 백준 2579 - 계단 오르기

'''
T = int(input())
dp = [[0]*3 for _ in range(T+1)]
st = [0]*(T+1)
for i in range(1,T+1):
    st[i] = int(input())
if T == 1:
    print(st[T])
    exit()

dp[1][1] = st[1]
dp[1][2] = 0
dp[2][1] = st[2]
dp[2][2] = st[1]+st[2]
for i in range(3,T+1):
    dp[i][1] = max(dp[i-2][1],dp[i-2][2])+st[i]
    dp[i][2] = dp[i-1][1]+st[i]

print(max(dp[T][1],dp[T][2]))
'''

