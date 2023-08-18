# 백준 2442 - 별 찍기 - 5

N = int(input())

for i in range(1, N+1):
    print(' ' * (N-i), end='')
    print('*' * i, end='')
    print('*' * (i-1))