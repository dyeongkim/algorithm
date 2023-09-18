# 백준 2231 - 분해합
N = int(input())
result = 0
for i in range(1, N+1):
    temp = i
    for j in str(temp):
        temp += int(j)
    if N == temp:
        result = i
        break

print(result)