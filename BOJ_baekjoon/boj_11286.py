# 백준 11286 - 절대값 힙
import heapq, sys

input = sys.stdin.readline
N= int(input())
hq = []

for _ in range(N):
    x = int(input())
    if x != 0:
        heapq.heappush(hq, (abs(x), x))
    else :
        if len(hq) <= 0 :
            print(0)
        else :
            print(heapq.heappop(hq)[1])