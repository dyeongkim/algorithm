# 백준 2309 - 일곱 난쟁이
import sys

input = sys.stdin.readline
N = [int(input()) for _ in range(9)]
N.sort()
temp = sum(N)
for i in range(8):
    for j in range(i+1, 9):
        if temp - N[i] - N[j] == 100:
            for k in range(9):
                if k != i and k != j:
                    print(N[k])
            
            exit()
