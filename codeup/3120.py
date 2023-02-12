a, b = map(int,input().split())
cnt = 0

temp = abs(b-a)

while temp != 0 :
    l = []
    for i in [10, 5, 1] :
        x = temp - i
        l.append(abs(x))
    temp = min(l)
    cnt += 1

print(cnt)
