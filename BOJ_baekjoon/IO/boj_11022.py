# 백준 11022 - A+B - 8

T = int(input())

for i in range(1, T+1, 1):
    A, B = map(int, input().split())
    print("Case #%d: %d + %d = %d" %(i, A, B, (A+B)))