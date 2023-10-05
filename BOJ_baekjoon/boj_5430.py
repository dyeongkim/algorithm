# 백준 5430 - AC
import sys
from collections import deque

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    S = input().rstrip()
    n = int(input())
    x = input().rstrip().replace("[","").replace("]","").split(",")
    result = deque()
    for i in x :
        if i =="":
            continue
        else :
            result.append(int(i))
    
    st = True

    for i in S :
        if i == "R" :
            result.reverse()
        elif i == "D" :
            if len(result) > 0 :
                result.popleft()
            else :
                st = False
                break
    if st :
        print(list(result))
    else :
        print("error")