# 백준 18111 - 마인크래프트
import sys

input = sys.stdin.readline
N, M, B = map(int,input().split())
ground = []
result = sys.maxsize

for _ in range(N):
    ground.append(list(map(int, input().split())))

for i in range(257):
    max_num, min_num = 0,0
    for j in range(N):
        for k in range(M):
            if ground[j][k] >= i :
                max_num += ground[j][k] - i
            else :
                min_num += i - ground[j][k]
    
    if max_num + B >= min_num:
        if min_num + (max_num*2) <= result :
            result = min_num + max_num*2

print(result, i)