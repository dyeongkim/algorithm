# 백준 2609 - 최대공약수와 최소공배수
import math
'''
A,B = map(int, input().split())
print(math.gcd(A,B))
print(math.lcm(A,B))
'''

A, B = map(int, input().split())

#최대 공약수 - A > B일때 B,A를 B로 나눈 나머지의 최대 공약수
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

#최소 공배수 - a,b 곱을 최대공약수로 나눈 값
def lcm(a, b):
    return a*b // gcd(a,b)