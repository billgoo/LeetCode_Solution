
class LRUCache:

    def __init__(self, capacity: 'int'):
        self.capacity = capacity
        self.hashmap = dict()

    def get(self, key: 'int') -> 'int':
        if key not in self.hashmap:
            return -1
        else:
            self.hashmap[key] = self.hashmap.pop(key)
            return self.hashmap[key]

    def put(self, key: 'int', value: 'int') -> 'None':
        if key in self.hashmap:
            self.hashmap.pop(key)
        else:
            if len(self.hashmap) == self.capacity:
                self.hashmap.pop(list(self.hashmap.keys())[0])
                
        self.hashmap[key] = value
                


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)