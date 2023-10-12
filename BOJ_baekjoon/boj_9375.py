# 백준 9375 - 패션왕 신해빈
import sys

input = sys.stdin.readline
n = int(input())

for _ in range(n):
    cnt = int(input())
    costume = {}
    ans = 1
    for i in range(cnt):
        cn, ct = input().split()
        if ct not in costume:
            costume[ct] = 1
        else :
            costume[ct] += 1
    
    for i in costume:
        ans *= (costume[i]+1)
    print(ans-1)