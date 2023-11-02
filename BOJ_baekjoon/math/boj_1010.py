# 백준 1010 - 다리 놓기
import sys

def fac(n):
    if n <= 1:
        return 1
    return n * fac(n-1)

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N, M = map(int,input().split())
    b = fac(M)//(fac(M-N)*fac(N))
    print(b)