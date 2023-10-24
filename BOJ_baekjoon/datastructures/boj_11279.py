# 백준 11279 - 최대 힙
import sys, heapq

input = sys.stdin.readline
N = int(input())
hq = []
for _ in range(N):
    x = int(input())
    if x == 0:
        if hq :
            print(heapq.heappop(hq)[1])
        else :
            print(0)
    else :
        heapq.heappush(hq, (-x,x))