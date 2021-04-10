# class HashTable {
#   constructor(size){
#     this.data = new Array(size);
#   }

#   _hash(key) {
#     let hash = 0;
#     for (let i =0; i < key.length; i++){
#         hash = (hash + key.charCodeAt(i) * i) % this.data.length
#     }
#     return hash;
#   }
# }

# const myHashTable = new HashTable(50);
# myHashTable.set('grapes', 10000)
# myHashTable.get('grapes')
# myHashTable.set('apples', 9)
# myHashTable.get('apples')

class HashTable:
    def __init__(self, size):
        self.size = size
        self.data = [[] for i in range(size)]

    def _hash(self, key):
        return len(key) % self.size

    def __str__(self):
        return str(self.__dict__)

    def set(self, key, value):
        self.data[self._hash(key)].append([key, value])

    def get(self, key):
        return self.data[self._hash(key)][0][1]

ht = HashTable(20)
ht.set('banana', 1200)
print(ht.get('banana'))

