# 백준 11050 - 이항 계수 1
import sys

input = sys.stdin.readline
N, K = map(int,input().split())

def fac(n):
    if n == 1 or n == 0:
        return 1
    else :
        return n * fac(n-1)

print(fac(N)//(fac(K)*fac(N-K)))