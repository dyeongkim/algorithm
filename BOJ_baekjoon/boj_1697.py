from collections import deque

graph = [0]*100001
N, K = map(int,input().split())


def bfs():
    queue = deque()
    queue.append(N)
	
    while queue:
        x=queue.popleft()
        if x == K:
            print(graph[x])
            break
        
        for i in [x+1, x-1, 2*x] :
            if 0 <= i < 100001 and not graph[i]:
                graph[i] = graph[x]+1
                queue.append(i)

bfs()