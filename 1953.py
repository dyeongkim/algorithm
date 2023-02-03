n = int(input())
print('*'*n)
def tri(n):
    if n == 1 :
        return '*'
    else :
        return tri(n-1) + '\n' + '*'*n

result = tri(n)
print(result)