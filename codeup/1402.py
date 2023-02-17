class Stack():
    def __init__(self):
        self.stack = []

    def push(self,data) :
        self.stack.append(data)

    def pop(self) :
        return str(self.stack.pop())

n = int(input())
data = list(map(int,input().split()))
st = Stack()

for i in data :
    st.push(i)

for i in range(n) :
    print(st.pop(), end=' ')