# 백준 10871 - X보다 작은 수

N, X = map(int,input().split())
A = list(map(int,input().split()))
result = []

for i in range(N):
    if A[i] < X :
        result.append(A[i])

for i in result :
    print(i, end=' ')