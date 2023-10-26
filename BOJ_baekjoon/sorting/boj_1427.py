# 백준 1427 - 소트인사이드
N = " ".join(input()).split(" ")
N.sort(reverse=True)
N = "".join(N)
print(N)