class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.back = None
        self.length = 0

    def enqueue(self, value):
        # appending instead of prepending like for the stack
        new_node = Node(value)
        if not self.front:
            self.front = new_node
            self.back = self.front
        else:
            self.back.next = new_node
            self.back = new_node
        
        self.length += 1
    def dequeue(self):
        # remove from the front of the line
        if not self.front:
            return None

        front = self.front.value
        self.front = self.front.next

        if not self.front:
            self.back = self.front
        return front

    def peek(self):
        return self.front.value

    def __str__(self):
        cur = self.front
        arr = []
        while cur:
            arr.append(cur.value)
            cur = cur.next

        return str(arr)

q = Queue()
q.enqueue('sam')
q.enqueue('tim')
q.enqueue('clarence')

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.back)
print(q)