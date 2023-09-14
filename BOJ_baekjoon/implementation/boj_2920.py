# 백준 2920 - 음계

M = list(map(int, input().split()))

for i in range(1,9):
    if M[i-1] != i :
        break

    if i == 8 :
        print("ascending")
        exit()

for i in range(1,9):
    if M[i-1] != 9-i :
        break

    if i == 8 :
        print("descending")
        exit()

print("mixed")
    