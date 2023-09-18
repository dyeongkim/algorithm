# 백준 1874 - 스택 수열
import sys

input = sys.stdin.readline
n = int(input())
num_list = [int(input()) for _ in range(n)]
cnt = 1
num = []
ans = []
for i in range(n):
    while cnt <= num_list[i]:
        num.append(cnt)
        ans.append("+")
        cnt += 1
    
    if num_list[i] == num[-1]:
        num.pop()
        ans.append("-")
    else :
        break    
    
if num :
    print("NO")
else :
    for i in ans:
        print(i)