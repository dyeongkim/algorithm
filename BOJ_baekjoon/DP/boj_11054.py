# 백준 11054 - 가장 긴 바이토닉 부분 수열

N = int(input())
A = list(map(int, input().split()))
dp_a = [0] * N
dp_d = [0] * N
result = [0] * N

for i in range(N) :
    for j in range(i) :
        if A[i] > A[j] and dp_a[i] < dp_a[j] :
            dp_a[i] = dp_a[j]
    dp_a[i] += 1
    for j in range(i+1, N):
        if A[i] < A[j] and dp_d[i] < dp_d[j]:
            dp_d[i] = dp_d[j]

for i in range(N):
    result[i] = dp_a[i] + dp_d[i]

print(max(result))