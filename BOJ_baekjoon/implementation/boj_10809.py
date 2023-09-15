# 백준 10809 - 알파벳 찾기

S = input()
m = [-1] * 123
for i in range(len(S)):
    if m[ord(S[i])] == -1 :
        m[ord(S[i])] = i

for i in range(97, 123):
    print(m[i], end=' ')