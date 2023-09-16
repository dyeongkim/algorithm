# 백준 10816 - 숫자 카드 2
import sys

input = sys.stdin.readline
N = int(input())
N_num = list(map(int,input().split()))
num = {}
M = int(input())
M_num = list(map(int,input().split()))

for i in N_num :
    if i in num :
        num[i] += 1
    else :
        num[i] = 1

for i in M_num :
    if i in num :
        print(num[i])
    else :
        print(0)