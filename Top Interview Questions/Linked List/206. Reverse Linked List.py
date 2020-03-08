# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        # recursive O_n time and O_n space
        if not head or not head.next:
            return head
        
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        
        return p
        """
        
        # iterative O_n time and O_1 space
        prev, curr = None, head
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp
            
        return prev
    