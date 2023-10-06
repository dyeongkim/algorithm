# 백준 5525 - IOIOI
import sys

input = sys.stdin.readline
N = int(input())
M = int(input())
S = input().rstrip()
cnt = 0
idx = 0
result = 0
while idx < (M-2):
    if S[idx:idx+3] == "IOI":
        cnt += 1
        idx += 2
        if cnt == N:
            result += 1
            cnt -= 1
    else :
        idx += 1
        cnt = 0

print(result)

    