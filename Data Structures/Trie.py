class TrieNode:

    def __init__(self, value=None):
        self.value = value
        self.end = False
        self.next = {}

    def __str__(self):
        return str(self.__dict__)

class Trie:

    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, word):
        cur = self.root
        index = 0

        while index < len(word):
            # check if the charcter is in the next dictionary
            # if it is, move to the TrieNode in the value
            # otherwise, add a new entry in the dictionary
            # create a new TrieNode as the value and set it to the current node
            if word[index] in cur.next:
                cur = cur.next[word[index]]
            else:
                new_node = TrieNode(word[index])
                cur.next[word[index]] = new_node
                cur = new_node
            
            index += 1

        cur.end = True


    def is_word(self, word):
        cur = self.root

        for c in word:
            if c in cur.next:
                cur = cur.next[c]
            else:
                return False

        return cur.end


    def is_prefix(self, prefix):
        cur = self.root

        for c in prefix:
            if c in cur.next:
                cur = cur.next[c]
            else:
                return False
        
        return not cur.end

    def starts_with(self, prefix):
        # start at the root node
        # traverse down the nodes until we reach the end of the given prefix
        # then we need to DFS down all possible paths, keeping track of every word we see
        # while loop to the last node of the prefix
        # then loop through keys in the next dictionary
        # call helper recursion across every node
        # base case: reach a null node - cur.next == {}
        # recursive case: cur.next != {}
        # how do we get closer to the answer?
        # iterate through the keys in the next dictionary, calling recursively for each key
        # action: add to our path string, if the cur.end == True, then add to our list of words
        
        current = self.root
        result = []
        for c in prefix:
            if c in current.next:
                current = current.next[c]
            else:
                return result

        def traverse(cur, curpath):
            # declare nonlocals
            nonlocal result, current

            # base case
            # one thing I am thinking about now is do we want to move to a none node
            # so if next is empty, call traverse on None
            if not cur:
                return

            # action: add to our current string, but check that we are not on the last node of the prefix
            if not cur == current:
                curpath += cur.value
            if cur.end:
                result.append(curpath)

            # check if the next dictionary is empty
            if cur.next == {}:
                traverse(None, curpath)
            else:
                # recursive case: iterate through the next dictionary and call traverse
                # across all nodes
                for key in cur.next.keys():
                    traverse(cur.next[key], curpath)
        
        traverse(current, prefix)
        return result

    def remove(self, word):
        # TODO: Add remove functionality
        pass
    
    def __str__(self):
        return str(self.__dict__)

trie = Trie()
trie.insert('hat')
trie.insert('ham')
trie.insert('hate')
trie.insert('hater')
trie.insert('hamster')
print(trie.starts_with('ha'))