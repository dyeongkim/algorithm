# 백준 1316 -  그룹 단어 체커

def chk(li):
    al_map = [True]*26
    temp = ''
    for i in li:
        if al_map[ord(i)-97] or i == temp:
            temp = i
            al_map[ord(i)-97] = False
        else :
            return False


    return True

N = int(input())
cnt = 0

for i in range(N):
    word = input()
    if chk(word):
        cnt += 1

print(cnt)