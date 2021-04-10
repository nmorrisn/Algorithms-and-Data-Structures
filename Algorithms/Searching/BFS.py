class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def __str__(self):
        return str(self.__dict__)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
        else:
            # need to traverse down the tree until we find where to put the new node
            cur = self.root
            while cur:
                if new_node.value > cur.value:
                    # go right
                    if not cur.right:
                        # add new node to the right
                        cur.right = new_node
                        break
                    cur = cur.right
                else:
                    # go left
                    if not cur.left:
                        cur.left = new_node
                        break
                    cur = cur.left

    def lookup(self, value):
        cur = self.root
        while cur:
            if cur.value == value:
                # found it, return the node
                return cur
            elif value > cur.value:
                # if its bigger, go right
                cur = cur.right
            else:
                # otherwise, go left
                cur = cur.left
        # if we didn't find it before we hit the end of the tree, return None
        return None

    def bfs(self):
        cur = self.root
        out = []
        nodes = []
        nodes.append(cur)

        while len(nodes) > 0:
            cur = nodes[0]
            del nodes[0]
            out.append(cur.value)

            if cur.left:
                nodes.append(cur.left)
            
            if cur.right:
                nodes.append(cur.right)
        
        return out

    def __str__(self):
        return str(self.__dict__)

tree = BST()
tree.insert(10)
tree.insert(12)
tree.insert(8)
tree.insert(100)
tree.insert(200)
print(tree.bfs())