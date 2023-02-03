n = int(input())

def bitnum(n) :
    if n <= 1 :
        return str(n)
    else : 
        return bitnum(n//2)+str(n%2)

print(bitnum(n))
