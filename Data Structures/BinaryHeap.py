class Heap:

    def __init__(self, type='min'):
        self.storage = []
        self.type = type

    # Time Complexity: O(1)
    # Auxiliary Space Complexity: O(1)
    def compare(self, a, b):
        if self.type == 'min':
            return self.storage[a] < self.storage[b]
        else:
            return self.storage[a] > self.storage[b]

    # Time Complexity: O(1)
    # Auxiliary Space Complexity: O(1)
    def swap(self, index1, index2):
        self.storage[index1], self.storage[index2] = self.storage[index2], self.storage[index1]

    # Time Complexity: O(1)
    # Auxiliary Space Complexity: O(1)
    def peak(self):
        return self.storage[0]

    # Time Complexity: O(1)
    # Auxiliary Space Complexity: O(1)
    def size(self):
        return len(self.storage)

    # Time Complexity: O(logn)
    # Auxiliary Space Complexity: O(1)
    def insert(self, value):
        # insert at the end of the list
        # bubbleup to correct position in heap
        self.storage.append(value)
        if self.size() > 1:
            self.bubble_up(self.size() - 1)

    # Time Complexity: O(logn)
    # Auxiliary Space Complexity: O(1)
    def bubble_up(self, index):
        # compare current index to parent
        # if true, swap the elements
        parent = self.get_parent(index)
        while index > 0 and self.compare(index, parent):
            self.swap(index, parent)
            index = parent
            parent = self.get_parent(index)

    def get_parent(self, index):
        if index % 2 == 0:
            return int((index - 2)/2)
        else:
            return int((index - 1)/2)

    def get_child(self, index):
        child1 = 2*index + 1
        child2 = 2*index + 2
        
        if child1 > self.size()-1:
            return None
        else:
            if child2 <= self.size()-1:
                if self.type == 'min':
                    if self.storage[child1] < self.storage[child2]:
                        return child1
                    else:
                        return child2
                else:
                    if self.storage[child1] > self.storage[child2]:
                        return child1
                    else:
                        return child2
            else:
                return child1

    # Time Complexity: O(logn)
    # Auxiliary Space Complexity: O(1)
    def remove_peak(self):
        # swap the first and last element
        # pop the last element
        # bubble down the new root
        self.swap(0, self.size() - 1)
        peak = self.storage.pop()
        self.bubble_down(0)
        return peak

    # Time Complexity: O(logn)
    # Auxiliary Space Complexity: O(1)
    def bubble_down(self, index):
        # compare smallest/largest child to current index
        # if child is smaller/larger than current index, swap
        # continue swapping until we reach the end of the list or the parent is in the right place
        child = self.get_child(index)
        while child and self.compare(child, index):
            self.swap(index, child)
            index = child
            child = self.get_child(index)

    # Time Complexity: O(n)
    # Auxiliary Space Complexity: O(1)
    def remove(self, value):
        # first find the value in the heap
        # keep track of the index
        # swap the element with the bottom of the heap
        # pop the element
        # bubbleup and bubbledown the index we removed
        index = -1

        for i in range(self.size()):
            if self.storage[i] == value:
                index = i

        if index < 0:
            return None

        # if we are removing the last element, we don't have to do anything but return the value
        if index == self.size() - 1:
            return self.storage.pop()

        self.swap(index, self.size()-1)
        out = self.storage.pop()

        self.bubble_up(index)
        self.bubble_down(index)

        return out

    def __str__(self):
        return str(self.__dict__)



############################################################
###############  DO NOT TOUCH TEST BELOW!!!  ###############
############################################################

# custom assert function to handle tests
# input: count {List} - keeps track out how many tests pass and how many total
#        in the form of a two item array i.e., [0, 0]
# input: name {String} - describes the test
# input: test {Function} - performs a set of operations and returns a boolean
#        indicating if test passed
# output: {None}
def expect(count, name, test):
    if (count is None or not isinstance(count, list) or len(count) != 2):
        count = [0, 0]
    else:
        count[1] += 1

    result = 'false'
    error_msg = None
    try:
        if test():
            result = ' true'
            count[0] += 1
    except Exception as err:
        error_msg = str(err)

    print('  ' + (str(count[1]) + ')   ') + result + ' : ' + name)
    if error_msg is not None:
        print('       ' + error_msg + '\n')

# compare if two flat lists are equal
def lists_equal(lst1, lst2):
    if len(lst1) != len(lst2):
        return False
    for i in range(0, len(lst1)):
        if lst1[i] != lst2[i]:
            return False
    return True