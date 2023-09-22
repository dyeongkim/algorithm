# 백준 1074 - Z

def recur(i, x, y) :
    global result
    if x == r and y == c :
        print(result)
        exit()
    if i == 1:
        result += 1
        return
    if not (x <= r < x+i and y <= c < y+i):
        result += i*i
        return
    temp = i // 2
    recur(temp, x, y)
    recur(temp, x, y+temp)
    recur(temp, x+temp, y)
    recur(temp, x+temp, y+temp)

N, r, c = map(int, input().split())
result = 0

recur(2**N, 0, 0)
print(result)