"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        
        # insert and copy next pointer
        dummy = head
        while dummy:
            temp = dummy.next
            # add deep copy of current node to the list
            dummy.next = Node(dummy.val, temp, None)
            
            dummy = dummy.next.next
            
        # copy random pointer
        dummy = head
        while dummy:
            # A'.random = C', A.random = C, C.next = C'
            dummy.next.random = dummy.random.next if dummy.random else None
            dummy = dummy.next.next
            
        # separate the list
        old, new = head, head.next
        result = head.next
        while new:
            old.next = new.next
            new.next = new.next.next if new.next else None
            
            old = old.next
            new = new.next
        
        return result
            