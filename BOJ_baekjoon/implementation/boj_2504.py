# 백준 2504 - 괄호의 값
import sys
input = sys.stdin.readline

S = list(input())

stack = []
result = 0
tmp = 1
for i in range(len(S)):

    if S[i] == "(":
        stack.append(S[i])
        tmp *= 2

    elif S[i] == ")":
        if not stack or stack[-1] == "[":
            result == 0
            break
        if S[i-1] == "("
            result += tmp
        stack.pop()
        tmp //=2
        