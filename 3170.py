'''
진짜 오랜만에 주현이 엄마는 기억력 테스트를 하기로 했다.

주현이가 많이 컸기 때문에 이제 숫자만 가지고 테스트하기엔 부족하다.

이번에도 N개의 숫자를 불러주고, M개의 질문을 한다.

처음에 [단어]와 [숫자]를 불러주고, 질문으로 [단어]를 물어보면 해당 단어의 [숫자]를 말하는 것이다.

그런데 불러 줄 때 같은 [단어]가 나오는 경우 [이전 단어]의 [숫자]에 [현재 숫자]를 더해야 한다.

예를 들어 "ddobot 3" , "poketmon 5", "ddobot 7"을 불러 주고, 질문으로 "ddobot"을 물었을 경우 3+7인 10을 답해야 한다.

이번에는 포켓몬 썬&문  카드 풀 팩이 걸려 있다. 주현이가 잘 할 수 있도록 도와주자.
'''

n,m = map(int,input().split())

d = {}

for i in range(n):
    s, k = map(str, input().split())
    if s in d :
        d[s] = int(k)+d.get(s)
    else :
        d[s] = int(k)


for i in range(m) :
    q = input()
    if q in d :
        print(d.get(q))
    else :
        print(0)
