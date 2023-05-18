# 백준 1966 - 프린터 큐
from collections import deque

K = int(input())

for i in range(K):
    N, M = map(int,input().split())
    queue = deque(map(int, input().split()))

    print(queue)
    while queue :
        print(queue.popleft())