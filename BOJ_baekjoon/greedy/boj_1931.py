# 백준 1931 - 회의실 배정

import sys

input = sys.stdin.readline
N = int(input())
result = 0
time = 0
room = []
for _ in range(N):
    room.append(list(map(int, input().split())))

room.sort(key = lambda x : (x[1],x[0]))

for s, e in room :
    if s >= time :
        time = e
        result += 1

print(result)