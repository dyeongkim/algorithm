# 백준 18870 - 좌표 압축
N = int(input())
X = list(map(int, input().split()))
S = sorted(list(set(X)))
dic = {S[i] : i for i in range(len(S))}
for i in X:
    print(dic[i], end=' ')