# 백준 1654 - 랜선 자르기
import sys

input = sys.stdin.readline
K, N = map(int, input().split())
lan = [int(input()) for _ in range(K)]

st, ed = 1, max(lan)

while st <= ed :
    mid = (st + ed)//2
    cnt = 0
    for i in lan:
        cnt += i//mid

    if  cnt >= N :
        st = mid + 1
    else :
        ed = mid - 1

print(ed)