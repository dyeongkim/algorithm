# 백준 28113 - 정보섬의 대중교통
N, A, B = map(int, input().split())

if A < max(N, B) :
    print("Bus")
elif A == max(N, B) :
    print("Anything")
else :
    print("Subway")