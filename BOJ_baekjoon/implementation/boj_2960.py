# 백준 2960 - 에라토스테네스의 체
import sys
input = sys.stdin.readline

N, K = map(int,input().split())

ans = [True]*(N+1)
result = 0
for i in range(2, N+1):
    for j in range(i, N+1, i):
        if ans[j] == True :
            ans[j] = False
            result += 1
            if result == K :
                print(j)
                exit()