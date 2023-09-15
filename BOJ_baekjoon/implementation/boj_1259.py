# 백준 1259 - 팰린드롬수

import math

while True :
    S = input().rstrip()
    if S == '0' :
        exit()

    result = "yes"
    for i in range(math.ceil(len(S)/2)):
        if S[i] != S[-(i+1)] :
            result = "no"
            break
    print(result)
