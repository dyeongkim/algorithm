# 백준 9086 - 문자열
import sys

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    S = input().rstrip()
    print(S[0],S[-1],sep="")