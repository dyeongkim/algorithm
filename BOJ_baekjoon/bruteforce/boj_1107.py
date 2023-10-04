# 백준 1107 - 리모컨
import sys

input = sys.stdin.readline
N = int(input())
M = int(input())
errorNum = set(map(int,input().split()))
if N == 100 :
    print(0)
    exit()

mincnt = abs(N - 100)

for i in range(1000001):
    nums = str(i)
    for j in range(len(nums)):
        if int(nums[j]) in errorNum :
            break
        elif j == len(nums)-1:
            mincnt = min(mincnt, abs(N-i)+len(nums))

print(mincnt)