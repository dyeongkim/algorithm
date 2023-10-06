# 백준 5430 - AC
import sys
from collections import deque

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    S = input().rstrip()
    n = int(input())
    x = input().rstrip()
    if n == 0 :
        result = deque()
    else :
        x = x[1:-1].split(",")
        result = deque(x)
    
    cnt_r = 0
    st = True
    for i in S :
        if i == "R" :
            cnt_r += 1
        elif i == "D" :
            if len(result) > 0 :
                if cnt_r % 2 != 0:
                    result.pop()
                else :
                    result.popleft()
            else :
                st = False
                break
    if cnt_r % 2 != 0:
        result.reverse()
    if st :
        print("[" + ",".join(result) + "]")
    else :
        print("error")