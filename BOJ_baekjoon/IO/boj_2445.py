# 백준 2445 - 별 찍기 - 8

N = int(input())

for i in range(1, N*2):
    if i <= N :
        print('*' * i, end='')
        print(' ' * (N-i)*2, end='')
        print('*' * i)
    else :
        print('*' * (2*N-i), end='')
        print(' ' * (i-N)*2, end='')
        print('*' * (2*N-i))