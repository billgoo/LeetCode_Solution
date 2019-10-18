# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        b = h1 = ListNode(0)
        e = h2 = ListNode(0)
        
        while head:
            if head.val < x:
                h1.next = head
                h1 = h1.next
            else:
                h2.next = head
                h2 = h2.next
            head = head.next
        
        # key step
        # Last node of "after" list would also be ending node of the reformed list
        h2.next = None
        
        h1.next = e.next
        return b.next