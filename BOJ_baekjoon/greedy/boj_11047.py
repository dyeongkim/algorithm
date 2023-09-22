# 백준 11047 - 동전 0

N, K = map(int, input().split())
coin = []
cnt = 0

for _ in range(N):
    coin.append(int(input()))

coin.sort(reverse= True)

for i in coin:
    cnt += K//i
    K = K%i

print(cnt)