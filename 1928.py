n = int(input())

def col(n):
    print(int(n))
    if n == 1:
        return 
    elif n%2 == 1 :
        return col(3*n+1)
    elif n%2 != 1 :
        return col(n/2)

col(n)