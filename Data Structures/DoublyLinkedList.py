class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.__dict__)

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head

    def __str__(self):
        node = self.head
        arr = []
        while node:
            arr.append(node.value)
            node = node.next
        return str(arr)

    def append(self, value):
        node = Node(value)
        node.prev = self.tail
        self.tail.next = node
        self.tail = node

    def prepend(self, value):
        node = Node(value)
        node.next = self.head
        self.head.prev = node
        self.head = node

    def insert(self, index, value):
        if index == 0:
            self.prepend(value)
            return
        
        i = 0
        new_node = Node(value)
        pre_node = self.head

        while i != index-1:
            pre_node = pre_node.next
            i += 1

        ins_node = pre_node.next
        # add link to rest of list
        new_node.next = ins_node
        # add back link for node we are inserting at to new node
        ins_node.prev = new_node
        # add link from pre node to new node
        pre_node.next = new_node
        # add back link from new node to pre node
        new_node.prev = pre_node

    def remove(self, index):
        i = 0
        pre_node = self.head

        if index == 0:
            node = self.head
            self.head = self.head.next
            self.head.prev = None
            del node
            return

        # if we had the length, we could do this for the tail as well

        while i != index-1:
            pre_node = pre_node.next
            i += 1

        rem_node = pre_node.next
        post_node = rem_node.next

        pre_node.next = rem_node.next
        post_node.prev = pre_node
        del rem_node



ll = LinkedList(10)

ll.append(12)
ll.append(36)
ll.append(86)

ll.prepend(98)
ll.prepend(320)

ll.insert(1, 200)
ll.insert(0, 189)

print(ll)

node = ll.tail
while node:
    print(node)
    node = node.prev

