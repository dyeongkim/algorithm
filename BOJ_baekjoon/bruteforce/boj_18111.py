# 백준 18111 - 마인크래프트
import sys

input = sys.stdin.readline
N, M, B = map(int,input().split())
ground = []
result = sys.maxsize
floor = 0

for _ in range(N):
    ground.append(list(map(int, input().rstrip().split())))

for i in range(257):
    max_num, min_num = 0,0
    for j in range(N):
        for k in range(M):
            if ground[j][k] > i :
                max_num += ground[j][k] - i
            else :
                min_num += i - ground[j][k]
    
    if min_num > max_num + B:
        continue
    
    cnt = max_num + (min_num*2)

    if cnt <= result :
        result = cnt
        floor = i

print(result, floor)

# https://land-turtler.tistory.com/82
