class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        self.s1.append(x)

    def pop(self):
        self.peek()
        return self.s2.pop()

    def peek(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]        

    def empty(self):
        return not self.s1 and not self.s2


obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
print(obj.peek())

print(obj.s2)
obj.push(5)

print(obj.s1)
print(obj.s2)

obj.pop()
obj.pop()
obj.pop()
print(obj.peek())
obj.pop()
print(obj.peek())