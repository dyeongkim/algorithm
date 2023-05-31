# 백준 10866 -  덱
import sys
input = sys.stdin.readline

def push_front(x) :
    li.insert(0,x)

def push_back(x) :
    li.append(x)

def pop_front() :
    if em() == 1:
        return -1
    else :
        return li.pop(0)


def pop_back() :
    if em() == 1:
        return -1
    else :
        return li.pop()


def si() :
    return len(li)

def em() :
    if len(li)<1 :
        return 1
    else :
        return 0

def front():
    if em() == 1:
        return -1
    else :
        return li[0]

def back():
    if em() == 1:
        return -1
    else :
        return li[-1]


N = int(input())
li = []


for _ in range(N):
    temp = list(map(str,input().split()))

    if len(temp) > 1 :
        s,num = temp[0], int(temp[1])
        if s == 'push_front':
            push_front(num)
        elif s == 'push_back' :
            push_back(num)
    else :
        s = temp[0]
        if s == 'pop_front':
            print(pop_front())
        elif s == 'pop_back' :
            print(pop_back())
        elif s == 'size':
            print(si())
        elif s == 'empty' :
            print(em())
        elif s == 'front':
            print(front())
        elif s == 'back' :
            print(back())