# 백준 2522 - 별 찍기 - 12

N = int(input())

for i in range(1, 2*N):
    if i <= N :
        print(' ' * (N-i), end='')
        print('*' * i)
    else :
        print(' ' * (i-N), end='')
        print('*' * (2*N-i))