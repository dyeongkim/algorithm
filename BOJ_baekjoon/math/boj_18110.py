# 백준 18110 - solved.ac
import sys
input = sys.stdin.readline

def round(n):
    if n - int(n) >= 0.5 :
        return int(n)+1
    else :
        return int(n)


n = int(input())

if n:
    
    num = []
    result = 0
    temp = round(n*0.15)
    for _ in range(n):
        num.append(int(input().strip()))

    num.sort()

    if temp > 0 :
        print(round(sum(num[temp:-temp])/len(num[temp:-temp])))
    else:
        print(round(sum(num)/len(num)))
else :
    print(0)