class Stack:
    def __init__(self):
        self.data = []
        self.length = 0

    def push(self, value):
        self.data.append(value)
        self.length += 1

    def pop(self):
        self.length -= 1
        return self.data.pop()

    def peek(self):
        return self.data[self.length-1]

    def __str__(self):
        return str(self.data)

    def isEmpty(self):
        return self.data == []

stk = Stack()
print(stk.isEmpty())
stk.push(1)
stk.push(2)
stk.push(3)
stk.push(4)


print(stk.pop())
print(stk.pop())
print(stk.isEmpty())
print(stk)