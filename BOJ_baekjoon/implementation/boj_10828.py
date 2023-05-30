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
        return 0
    else :
        return  1

def to():
    if em():
        return -1
    else :
        return li[-1]

N = int(input())

for _ in range(N):
    temp = list(map(str,input().split()))

    if len(temp) > 1 :
        s, num = temp[0], int(temp[1])

        pu(num)
    else :
        
        if temp[0] == 'pop' :
            print(po())

        elif temp[0] == 'size' :
            print(si())

        elif temp[0] == 'empty' :
            print(em())
            
        elif temp[0] == 'top' :
            print(to())

