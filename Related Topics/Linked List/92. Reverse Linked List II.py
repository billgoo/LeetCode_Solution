# 92. Reverse Linked List II
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None

        curr, prev = head, None
        i = 1
        while i < left:
            prev, curr = curr, curr.next
            i += 1

        prev_dummy, tail = prev, curr
        while i <= right:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            i += 1

        tail.next = curr
        if not prev_dummy:
            # reverse from head
            return prev
        else:
            prev_dummy.next = prev
        return head