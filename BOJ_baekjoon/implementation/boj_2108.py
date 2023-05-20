# 백준 2108 - 통계학
import sys
input = sys.stdin.readline
def mean(li) :
    return round(sum(li)/len(li))

def median(li) :
    temp = li[:]
    temp.sort()
    return temp[len(temp)//2]

    
def mode(li) :
    li.sort()
    dic = dict()
    for i in li :
        if i in dic :
            dic[i] += 1
        else :
            dic[i] = 1
    max_num = max(dic.values())
    temp = []
    for i in dic:
        if max_num == dic[i]:
            temp.append(i)

            
    if len(temp) > 1:
        return temp[1]
    else :
        return temp[0]


def ran(li) :
    return max(li) - min(li)

N = int(input())

li = []
for i in range(N):
    li.append(int(input()))

print(mean(li))
print(median(li))
print(mode(li))
print(ran(li))