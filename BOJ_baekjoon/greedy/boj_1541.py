# 백준 1541 - 잃어버린 괄호
import sys

N = input().rstrip()
mi = N.split("-")
num = []
for i in mi :
    su = sum(map(int, i.split("+")))
    num.append(su)

result = num[0]
for i in range(1, len(num)):
    result -= num[i]
print(result)