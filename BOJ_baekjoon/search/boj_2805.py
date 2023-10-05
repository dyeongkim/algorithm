# 백준 2805 - 나무 자르기
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
tree = list(map(int, input().split()))
'''
tree.sort() # 나무 크기 순으로 정렬
st = 0
max_len = tree[-1]
ans = 0
while st <= max_len: # 나무 자를 높이 이분 탐색
    result = 0
    mid = (st+max_len) // 2

    t_St, t_ed = 0, N-1 # 자를 수 있는 나무 탐색 변수
    while t_St <= t_ed : # 현재 높이로 자를 수 있는 나무 최소 위치 이분탐색
        t_Mid = (t_St+t_ed) // 2
        if tree[t_Mid] < mid: # ex) 현재 높이 15 나무 리스트 [10, 15, 17, 20]일때 이분탐색해서 최소 나무 위치인덱스 t_ST
            t_St = t_Mid + 1
        else :
            t_ed = t_Mid - 1

    for i in range(t_St, N): # 최소 나무 위치인덱스 t_ST 부터 계산
        result += tree[i]-mid
    if result >= M :
        st = mid + 1
    else :
        max_len = mid - 1

print(max_len)
'''
st, ed = 0, max(tree)
while st <= ed :
    mid = (st + ed) // 2
    ans = 0

    for i in tree:
        if i >= mid :
            ans += i - mid

    if ans >= M:
        st = mid + 1
    else :
        ed = mid - 1

print(ed)