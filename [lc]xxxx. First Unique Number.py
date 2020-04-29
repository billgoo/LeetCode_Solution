## Hint 1: Use hashmap store double linked list
# Use doubly Linked list with hashmap of pointers to linked list nodes. 
# add unique number to the linked list. When add is called check if 
# the added number is unique then it have to be added to the linked list 
# and if it is repeated remove it from the linked list if exists. 
# When showFirstUnique is called retrieve the head of the linked list.
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.head = self.rear = DoubleLinkedListNode(-1)
        self.hashmap = dict()
        self.s = set()
        for n in nums:
            self.add(n)

            
    def showFirstUnique(self) -> int:
        # print(self.dummy)
        if self.head.next:
            return self.head.next.val
        else:
            return -1

        
    def add(self, value: int) -> None:
        # print(value)
        if value in self.s:
            node = self.hashmap[value]
            
            if node == self.rear:
                self.rear = self.rear.prev
                self.rear.next = None
            
            elif node != None:
                # remove node
                node.prev.next = node.next
                node.next.prev = node.prev
                
            self.hashmap[value] = None
        else:
            node = DoubleLinkedListNode(value)
            node.prev = self.rear
            self.rear.next = node
            self.rear = node
            
            self.hashmap[value] = node
            self.s.add(value)
        # return
        

        
class DoubleLinkedListNode:
    
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
        
        
# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)

## Hint 2: Use queue and check that first element of the queue is always unique.
"""
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.s = set()
        self.unique = set()
        self.q = []
        for n in nums:
            self.add(n)

    def showFirstUnique(self) -> int:
        while self.q:
            value = self.q[0]
            if value not in self.unique:
                self.q.pop(0)
            else:
                return value
        return -1

    def add(self, value: int) -> None:
        if value not in self.s:
            self.s.add(value)
            self.q.append(value)
            self.unique.add(value)
        else:
            if value in self.unique:
                self.unique.remove(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
"""

## Hint 3: Use set or heap to make running time of each function O(logn).