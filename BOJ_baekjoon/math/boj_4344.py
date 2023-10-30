# 백준 4344 - 평균은 넘겠지
import sys

input = sys.stdin.readline
C = int(input())

for _ in range(C):
    s = list(map(int, input().split()))
    avg = sum(s[1:]) / s[0]
    cnt = 0
    for i in s[1:]:
        if i > avg:
            cnt += 1
    
    print("%0.3f" % (round((cnt / s[0]) * 100, 3)),end="%\n")    