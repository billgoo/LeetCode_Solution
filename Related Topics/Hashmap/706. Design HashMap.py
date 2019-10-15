class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = 10000
        self.map = [None for i in range(self.m)]
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        i = key % self.m
        node = ListNode(key, value)
        if self.map[i] != None:
            cur = self.map[i]
            while cur:
                if cur.key == key:
                    cur.val = value
                    break
                cur = cur.next
            else:
                node.next = self.map[i]
                self.map[i] = node
        else:
            self.map[i] = node
        if i == 4146:
            c = self.map[i]
            while c:
                c = c.next
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        i = key % self.m
        cur = self.map[i]
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        else:
            return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        i = key % self.m
        cur = pre = self.map[i]
        if pre != None:
            if pre.key == key:
                self.map[i] = pre.next
            else:
                cur = cur.next
                while cur:
                    if cur.key == key:
                        pre.next = cur.next
                        break
                    cur = cur.next
                    pre = pre.next
        
        
class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)