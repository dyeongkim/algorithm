# 백준 6064 - 카잉 달력
import sys

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())
    ans = y
    while ans <= M*N:
        if (ans-x) % M == 0 and (ans-y) % N == 0:
            break
        ans += N

    if ans <= M*N :
        print(ans)
    else :
        print(-1)