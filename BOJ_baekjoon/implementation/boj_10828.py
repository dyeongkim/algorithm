#백준 10828 - 스택
import sys
input = sys.stdin.readline

li = []

def pu(x):
    li.append(x)

def po():
    if em():
        return -1
    else :
        return li.pop()

def si():
    return len(li)
def em():
    if len(li) > 0:
        return False
    else :
        return  True

def to():
    if em():
        return -1
    else :
        return li[-1]

N = int(input())

for _ in range(N):
    temp = map()