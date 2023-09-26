# 백준 28116 - 선택 정렬의 이동 거리

import sys

input = sys.stdin.readline
N = int(input())
num = list(map(int, input().split()))
num_copy = num[:]
result = [0] * N

for i in range(N):
    min_index = i
    for j in range(i, N):
        print(num)
        if num[min_index] > num[j]:
            min_index = j
    result[num_copy.index(num[i])] += (min_index - i)
    result[num_copy.index(num[min_index])] += (min_index - i)
    num[min_index], num[i] = num[i], num[min_index]
    print(result)

print(result)