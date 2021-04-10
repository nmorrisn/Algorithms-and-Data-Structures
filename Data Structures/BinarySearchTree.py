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
        # empty tree, just make it the root
        new_node = Node(value)
        if not self.root:
            self.root = new_node
        else:
            # traverse tree and insert as leaf
            pre_node = self.root
            while pre_node:
                # if new node is greater than pre node, go right
                if new_node.value > pre_node.value:
                    # if there is no right node, add our new node
                    if not pre_node.right:
                        pre_node.right = new_node
                        break
                    
                    # otherwise continue traversing
                    pre_node = pre_node.right
                else:
                    # if there is no left node, add our new node
                    if not pre_node.left:
                        pre_node.left = new_node
                        break
                    
                    # otherwise continue traversing
                    pre_node = pre_node.left

    def lookup(self, value):
        node = self.root
        while node:
            if value == node.value:
                return node
            elif value > node.value:
                node = node.right
            else:
                node = node.left

        return None

    def __str__(self):
        return str(self.__dict__)

bst = BST()

bst.insert(10)
bst.insert(12)
bst.insert(6)
bst.insert(7)
bst.insert(100)
bst.insert(200)
bst.insert(300)
print(bst.lookup(200).right)