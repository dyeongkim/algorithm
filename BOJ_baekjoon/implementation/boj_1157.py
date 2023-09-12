# 백준 1157 - 단어 공부
import sys

S = input()
S = S.upper()
M = [0]*91

for i in S :
    M[ord(i)] += 1

result = 0
for i in range(65, 91, 1):
    if max(M) == M[i]:
        if result != 0:
            print("?")
            exit()
        result = i

print(chr(result))