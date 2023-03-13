import sys
input = sys.stdin.readline

def add_node(a,b):
    graph[a] += [b]
    graph[b] += [a]

def dfs(start = 0):
    vis.add(start)
    for i in graph[start]:
        if i not in vis:
            dfs(i)

c = int(input())
e = int(input())
vis = set()

graph = [[] for _ in range(c)]


for i in range(e):
    x, y = map(int,input().split())
    add_node(x-1, y-1)


dfs()
print(len(vis)-1)