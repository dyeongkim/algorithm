# 백준 10992 - 별 찍기 - 17

N = int(input())

for i in range(1, N+1):
    print(' ' * (N-i), end='')
    print('*', end='')
    if i > 1 :
        if i == N :
            print('*' * ((i-1) * 2), end='')
        else :
            print(' ' * ((i-1)*2-1), end='')
            print('*', end='')
    print()