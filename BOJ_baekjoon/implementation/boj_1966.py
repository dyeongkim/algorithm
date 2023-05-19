# 백준 1966 - 프린터 큐
from collections import deque

K = int(input()) # 테스트 케이스

for i in range(K):
    N, M = map(int,input().split()) # 문서 개수, 원하는 문서 위치
    queue = deque(map(int, input().split())) # 문서 중요도
    idx = deque(list(range(N))) # 문서 순서
    result = 0 # 출력 카운트

    while queue :
        if max(queue) == queue[0] : # 큐에서 가장 큰 수가 가장 앞에 있을때
            result += 1 # 출력 카운트
            queue.popleft() # 큐 출력
            q_idx = idx.popleft() # 현재 출력된 큐 원래 위치
            if q_idx == M : # 원하는 문서 순서 체크
                print(result) #출력
        else : # 제일 큰 수가 아니면 뒤로 다시 넣기
            queue.append(queue.popleft()) 
            idx.append(idx.popleft())