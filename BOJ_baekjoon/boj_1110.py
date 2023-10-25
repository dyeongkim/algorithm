# 백준 1110 - 더하기 사이클

N = int(input())
temp = N
num = 0
ans = 0
if N < 10:
    num = N*10
    num = (num%10) + (num//10)
else :
    num = (N%10) + (N//10)
while True :
    num = ((temp%10)*10) + (num%10)
    ans += 1
    if (N == num):
        break
    temp = num
    num = (num%10) + (num//10)

print(ans)