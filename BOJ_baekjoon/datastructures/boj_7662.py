# 백준 7662 - 이중 우선순위 큐
import sys, heapq

input = sys.stdin.readline
T = int(input()) # 테스트 케이스

for _ in range(T):
    k = int(input()) # 입력받을 횟수
    hq_min = [] # 최소힙 초기화
    hq_max = [] # 최대힙 초기화
    num = {} # 원소 동기화용 dict
    for i in range(k):
        s, n = input().split()
        n = int(n)
        if s == "I": # 원소 삽입
            heapq.heappush(hq_min, n) # 최소힙에 삽입
            heapq.heappush(hq_max, (-n, n)) # 최대힙에 삽입
            if n in num : # 들어온적있는지 확인
                num[n] += 1 # 원소 개수 추가
            else :
                num[n] = 1 # 원소 초기화
        else :
            if n == -1 :
                while hq_min and num[hq_min[0]] < 1: # 최소힙에는 있는데 실제로는 없는 원소일경우 제거
                    heapq.heappop(hq_min) 
                if hq_min : 
                    num[hq_min[0]] -= 1
                    heapq.heappop(hq_min)

            else :
                while hq_max and num[hq_max[0][1]] < 1:# 최대힙에는 있는데 실제로는 없는 원소일경우 제거
                    heapq.heappop(hq_max)
                if hq_max :
                    num[hq_max[0][1]] -= 1
                    heapq.heappop(hq_max)
    
    # 최소힙, 최대힙에서 실제론 없는 원소가 존재하는경우 제거
    while hq_min and num[hq_min[0]] < 1: 
        heapq.heappop(hq_min)
    while hq_max and num[hq_max[0][1]] < 1:
        heapq.heappop(hq_max)

    if hq_max and hq_min :
        print(hq_max[0][1], hq_min[0])
    else: 
        print("EMPTY")