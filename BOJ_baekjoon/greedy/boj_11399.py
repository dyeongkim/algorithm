# 백준 11399 - ATM

N = int(input())
P = list(map(int,input().split()))

P.sort()

result = 0

for i in range(N) :
    num = sum([k for k in P[:i+1]])
    
    result += num

print(result)
