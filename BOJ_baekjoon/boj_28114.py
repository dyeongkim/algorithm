# 백준 28114 - 팀명 정하기
import sys

input = sys.stdin.readline
team = []

for _ in range(3):
    a, b, c = input().split()
    team.append((int(a), int(b), c))

num = ""
name = ""

team.sort(reverse=True)

for i in team :
    name += i[2][0]

team.sort(key= lambda x : x[1])

for i in team :
    num += str(i[1]%1000)

print(num)
print(name)