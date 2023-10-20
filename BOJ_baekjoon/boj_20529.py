# 백준 20529 - 가장 가까운 세 사람의 심리적 거리
import sys
from itertools import combinations

# 사람사이 거리 계산
def chk(a, b):
    result = 0
    for i, j in zip(a,b): # 동일한 개수로 이루어진 iterable 객체를 받아 묶어서 반환 ex) 123, 123 -> [1,1], [2,2], [3,3]
        if i != j:
            result += 1
    return result

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())
    mbti = input().rstrip().split()
    if N > 32 : # 비둘기집원리/ 16개 MBTI는 17명이면 무조건 2명은 겹치고 33명이상이면 3명은 겹침
        print(0)
    else :
        ans = 13
        p = combinations(mbti, 3) # 서로다른 n개중에서 r개 취해서 조합만드는 함수
        for a,b,c in p: # 서로다른 조합들에서 3명을 뽑아옴
            result = 0
            # 세사람 사이의 거리 계산
            result += chk(a, b) 
            result += chk(b, c)
            result += chk(a, c)

            ans = min(result, ans)
        
        print(ans)