# 백준 1620 - 나는야 포켓몬 마스터 이다솜
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
book = {}

for i in range(1, N+1):
    name = input().rstrip()
    if not name in book.keys():
        book.update({name : i})

num = list(book.keys())
for _ in range(M):
    temp = input().strip()
    try :
        print(num[int(temp)-1])
    except :
        print(book[temp])