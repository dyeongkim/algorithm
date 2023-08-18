# 백준 10991 - 별 찍기 - 16

N = int(input())

for i in range(1, N+1):
    print(' ' * (N-i), end='')
    print('*', end='')
    if i > 1 :
        for j in range(i-1):
            print(" *", end='')
    print()