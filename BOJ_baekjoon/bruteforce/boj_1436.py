# 백준 1436 - 영화감독 숌
N = int(input())

num = 666
while N > 1:
    num += 1
    if str(num).find('666') != -1:
        N -= 1

print(num)