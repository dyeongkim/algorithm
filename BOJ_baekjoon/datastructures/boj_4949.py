# 백준 4949 - 균형잡힌 세상

while True :
    S = input()
    st = []
    temp = True
    if S == '.':
        break

    for i in range(len(S)) :
        if S[i] == "(" or S[i] == "[" :
            st.append(S[i])
        elif S[i] == ")" :
            if len(st) != 0 :
                if st.pop() != "(" :
                    temp = False
                    break
            else :
                temp = False
                break
        elif S[i] == "]" :
            if len(st) != 0:
                if st.pop() != "[" :
                    temp = False
                    break
            else :
                temp = False
                break
    
    if st :
        temp = False

    if temp :
        print("yes")
    else :
        print("no")