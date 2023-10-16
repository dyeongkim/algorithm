# 백준 5597 - 과제 안 내신 분..?
import sys

input = sys.stdin.readline
num = [True]*31

for i in range(28):
    n = int(input())
    num[n] = False

for i in range(1, 31):
    if num[i]:
        print(i)