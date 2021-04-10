class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def push(self, value):
        new_node = Node(value)

        if not self.top:
            self.top = new_node
            self.bottom = self.top
        else:
            cur = self.top
            self.top = new_node
            self.top.next = cur

        self.length += 1

    def pop(self):
        if self.isEmpty():
            return None

        top = self.top.value
        self.top = self.top.next
        self.length -= 1

        if not self.top:
            self.bottom = self.top
        return top

    def peek(self):
        return self.top.value

    def __str__(self):
        arr = []
        node = self.top

        while node:
            arr.append(node.value)
            node = node.next

        return str(arr)

    def isEmpty(self):
        return self.top == None

stk = Stack()
stk.push(1)
stk.push(2)
stk.push(3)
stk.push(4)

print(stk.pop())
print(stk.pop())
print(stk.pop())
print(stk.pop())
print(stk.bottom)
print(stk)