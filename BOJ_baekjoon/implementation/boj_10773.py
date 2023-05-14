# 백준 10773 - 제로
li = []


K = int(input())

result = 0

for i in range(K) :
    n = int(input())

    if n == 0 :
        li.pop()
    else :
        li.append(n)

for i in li :
    result += i

print(result)