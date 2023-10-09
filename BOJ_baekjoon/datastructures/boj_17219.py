# 백준 17219 - 비밀번호 찾기
import sys

input = sys.stdin.readline
N, M = map(int,input().split())
pw = {}

for _ in range(N):
    s, p = input().split()
    pw[s] = p

for _ in range(M):
    s = input().rstrip()
    print(pw[s])
