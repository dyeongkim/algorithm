# 백준 15829 - Hashing

L = int(input())
a = input()
H = 0

for i in range(L):
    H += ((ord(a[i]) - 96) * (31**i))

print(H%1234567891)