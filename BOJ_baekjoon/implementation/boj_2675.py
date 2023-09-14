# 백준 2675 - 문자열 반복
import sys

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    R, S = input().split()
    for i in S:
        print(i*int(R), end='')

    print()
