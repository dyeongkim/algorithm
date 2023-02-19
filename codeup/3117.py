class Stack():
    def __init__(self):
        self.stack = []

    def push(self,data) :
        self.stack.append(data)

    def pop(self) :
        return self.stack.pop()

n = int(input())
st = Stack()

for i in range(n) :
    x = int(input())
    if x == 0:
        st.pop()
    else:
        st.push(x)

result = 0

while st.stack:
    result += st.pop()

print(result)

