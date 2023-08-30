# 백준 1912 - 연속합

n = int(input())
num = list(map(int, input().split()))
dp = [0] * n

10 -4 3 1 5 6 -35 12 21 -1
10 6 9 10 15 21 -14 -2 19 -1
6 -1 
for i in range(n) :
    tot = 0
    for j in range(i) :
