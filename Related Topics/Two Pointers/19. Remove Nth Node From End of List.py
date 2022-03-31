# 19. Remove Nth Node From End of List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p = head
        dummy = ListNode(-1)
        dummy.next = head
        parent = dummy

        for _ in range(n):
            p = p.next

        while p:
            p = p.next
            parent = parent.next
        parent.next = parent.next.next
        return dummy.next