# 백준 1389 - 케빈 베이컨의 6단계 법칙
import sys
from collections import deque
def add_edge(a, b):
    graph[a].append(b)
    graph[b].append(a)

def bfs(s):
    visited = [s]
    queue = deque()
    num = [0]*(N+1)
    queue.append(s)
    while queue :
        a = queue.popleft()
        for i in graph[a] :
            if i not in visited:
                num[i]= num[a]+1
                visited.append(i)
                queue.append(i)
    return sum(num)


input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
ans = sys.maxsize
result = []
for _ in range(M):
    a,b = map(int, input().split())
    add_edge(a, b)

for i in range(1, N+1):
    result.append(bfs(i))

print(result.index(min(result))+1)