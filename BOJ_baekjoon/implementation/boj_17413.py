# 백준 17413 - 단어 뒤집기2
import sys
input = sys.stdin.readline

S = list(input().rstrip())

i = 0
st = 0

while i < len(S):
    if S[i] == "<":
        i += 1
        while S[i] != ">":
            i += 1
        i += 1
    elif S[i].isalnum():
        st = i
        while i <len(S) and S[i].isalnum():
            i += 1
        temp = S[st:i]
        temp.reverse()
        S[st:i] = temp
    else :
        i += 1

print("".join(S))