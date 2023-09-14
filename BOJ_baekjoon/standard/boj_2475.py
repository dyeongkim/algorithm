# 백준 2475 - 검증수
import sys

A,B,C,D,E = map(int, input().split())
print(((A**2)+(B**2)+(C**2)+(D**2)+(E**2)) % 10)