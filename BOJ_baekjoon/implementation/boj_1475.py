# 백준 1475 -  방 번호
import sys
input = sys.stdin.readline

m = [0] * 10
N = input().strip()

for i in N :
    num = int(i)
    if num == 6 or num == 9 :
        if m[6] <= m[9]:
            m[6] += 1
        else :
            m[9] += 1
    else :
        m[num] += 1

print(max(m))
