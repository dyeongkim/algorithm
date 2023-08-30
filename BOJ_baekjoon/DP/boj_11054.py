# 백준 11054 - 가장 긴 바이토닉 부분 수열

N = int(input())
A = list(map(int, input().split()))
dp_a = [1] * N
dp_d = [1] * N
result = [0] * N

for i in range(N) :
    for j in range(i) :
        if A[i] > A[j] :
            dp_a[i] = max(dp_a[i], dp_a[j]+1)
    
for i in range(N-1, -1, -1) :
    for j in range(N-1,i-1, -1) :
        if A[i] > A[j] :
            dp_d[i] = max(dp_d[i], dp_d[j]+1)


for i in range(N):
    result[i] = dp_a[i] + dp_d[i]

print(max(result)-1)