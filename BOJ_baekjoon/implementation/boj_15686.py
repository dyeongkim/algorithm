# 백준 15686 - 치킨 배달
import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)] # 마을 지도
result = N**3*2
h_list = [] # 집 위치 리스트
c_list = [] # 치킨집 위치 리스트

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1: # 집 위치 저장
            h_list.append((i,j))
        elif graph[i][j] == 2: # 치킨집 위치 저장
            c_list.append((i,j))

for chi in combinations(c_list, M): # c_list에서 M개 취하여 조합 만들기
    temp = 0 # 치킨집 총 거리
    for h in h_list:
        chi_len = N**2*len(h_list) # 집에서 치킨집까지 거리
        for i in range(M):
            chi_len = min(chi_len,abs(h[0] - chi[i][0])+abs(h[1] - chi[i][1])) # 거리 계산 abs(cx - hx)+abs(cy-hy)
        temp += chi_len
    result = min(result, temp)
print(result)