# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        
        slow = head
        fast = head.next
        
        # find if we have cycle and get meet point
        while slow != fast:
            if not fast or not fast.next:
                return None
            slow = slow.next
            fast = fast.next.next
            
        # slow from head and fast from meet point both at one step
        slow = head
        fast = fast.next
        while slow != fast:
            slow = slow.next
            fast = fast.next
            
        return slow
        