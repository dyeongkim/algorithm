# 백준 4949 - 균형잡힌 세상
import sys
input = sys.stdin.readline

while True :
	S = input()
	st = []
	temp = True
       
    if S == ".":
        break
	
    for i in range(len(S)) :
        if S[i] == "(" or S[i] == "[" :
            st.append(S[i])
        elif S[i] == ")" and st.pop() != "(" :
            temp = False
            break
        elif S[i] == "]" and st.pop() != "[":
            temp = False
            break
    if temp :
	    print("yes")
    else :
        print("no")