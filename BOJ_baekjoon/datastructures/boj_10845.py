# 백준 10845 - 큐
import sys

input = sys.stdin.readline
N = int(input())
queue = []

def push(n) :
    queue.append(n)

def pop():
    if len(queue) > 0:
        print(queue.pop(0))
    else :
        print(-1)
    
def size():
    print(len(queue))

def empty():
    if len(queue) > 0:
        print(0)
    else :
        print(1)

def front():
    if len(queue) > 0:
        print(queue[0])
    else :
        print(-1)

def back():
    if len(queue) > 0:
        print(queue[-1])
    else :
        print(-1)

for _ in range(N):
    S = input().split()

    if len(S) > 1:
        push(S[1])
    else:
        if S[0] == 'pop':
            pop()
        elif S[0] == 'size':
            size()
        elif S[0] == 'empty':
            empty()
        elif S[0] == 'front':
            front()
        elif S[0] == 'back':
            back()