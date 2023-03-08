from collections import deque
import sys

class graph():
    def __init__(self):
        self.list = {}
        
    def add_edge(self, a, b):
        if a not in self.list:
            self.list[a] = []
        self.list[a].append(b)
        if b not in self.list:
            self.list[b] = []
        self.list[b].append(a)
        
    def dfs(self, start, vis=set()):
        vis.add(start)
        print(start, end=' ')
        
        if start in self.list:
            for n in self.list[start]:
                if n not in vis:
                    
    
    def bfs(self, start, vis=set()):
        






input = sys.stdin.readline
N, M, V = map(int,input().split())


for i in range(M):
    add