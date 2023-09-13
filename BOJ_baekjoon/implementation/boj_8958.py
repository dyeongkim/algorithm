# 백준 8958 - OX퀴즈
import sys

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    S = input()
    score = 0
    b = 1
    
    for i in S :
        if i == "O":
            score += b
            b += 1
        else :
            b = 1

    print(score)