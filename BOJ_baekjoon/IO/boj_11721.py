# 백준 11721 - 열 개씩 끊어 출력하기


N = input()
for i in range(0, len(N), 10) :
    print(N[i:i+10])