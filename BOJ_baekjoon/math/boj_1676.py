# 백준 1676 - 팩토리얼 0의 개수

def fac(n):
    if n <= 1 :
        return 1
    else :
        return n * fac(n-1)

N = int(input())

num = str(fac(N))
cnt = 0

for i in range(len(num)-1, -1, -1):
    if num[i] != '0':
        break
    else :
        cnt += 1

print(cnt)