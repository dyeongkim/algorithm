# 백준 2164 - 카드2
import sys
from collections import deque

input = sys.stdin.readline
queue = deque()
N = int(input())
st = True

for i in range(1, N+1):
    queue.append(i)

while len(queue) > 1:
    if st :
        queue.popleft()
        st = False
    else :
        queue.append(queue.popleft())
        st = True
print(queue.pop())