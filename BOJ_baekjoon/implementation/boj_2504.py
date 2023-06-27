# 백준 2504 - 괄호의 값
S = list(input())

stack = []
result = 0
tmp = 1
for i in range(len(S)):
    if S[i] == "(":
        stack.append(S[i])
        tmp *= 2
    
    elif S[i] == "[":
        stack.append(S[i])
        tmp *= 3

    elif S[i] == ")":
        if not stack or stack[-1] == "[":
            result = 0
            break

        if S[i-1] == "(" :
            result += tmp
        stack.pop()
        tmp //=2
    
    else :
        if not stack or stack[-1] == "(":
            result = 0
            break

        if S[i-1] == "[":
            result += tmp
        
        stack.pop()
        tmp //= 3


if stack:
    print(0)
else :
    print(result)        