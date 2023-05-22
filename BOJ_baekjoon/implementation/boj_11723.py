# 백준 11723 - 집합

import sys
input = sys.stdin.readline

M = int(input())
result = set()

for i in range(M):
    temp = input().strip().split()

    if len(temp) == 1 :
        if temp[0] == "all" :
            result = set([_ for _ in range(1,21)])
        else :
            result = set()
    else :
        S, N = temp[0],int(temp[1])
        if S == 'add' :
            if N not in result :
                result.add(N)
        elif S == 'remove' :
            if N in result :
                result.discard(N)
        elif S == 'check' :
            if N in result :
                print(1)
            else :
                print(0)
        elif S == 'toggle' :
            if N in result :
                result.discard(N)
            else :
                result.add(N)