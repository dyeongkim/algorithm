# 백준 3052 - 나머지
import sys

input = sys.stdin.readline
num = []

for _ in range(10):
    temp = int(input())%42
    if not temp in num :
        num.append(temp)

print(len(num))