# 백준 11866 - 요세푸스 문제 0

N, K = map(int,input().split())
li = [i for i in range(1, N+1)]
ans = []
idx = 0

while li:
    idx += K-1
    if idx >=len(li) :
        idx = idx%len(li)
    ans.append(str(li.pop(idx)))



print("<",", ".join(ans),">",sep="")