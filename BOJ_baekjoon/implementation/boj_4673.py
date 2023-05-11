# 백준 4673 -  셀프 넘버
def selfnum(n):
    temp = n
    for i in str(n):
        temp += int(i)
    if temp <= 10000:
        result[temp] = False


result = [True]*10001
for i in range(1,10001):
    selfnum(i)

for i in range(1,10001):
    if result[i]:
        print(i)
 