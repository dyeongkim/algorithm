n = int(input())

def col(n):
    if n == 1:
        return print(int(n))
    elif n%2 == 1 :
        col(3*n+1)
    elif n%2 != 1 :
        col(n/2)
    return print(int(n))

col(n)
