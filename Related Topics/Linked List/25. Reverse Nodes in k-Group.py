# 25. Reverse Nodes in k-Group
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        dummy = tailGroup = ListNode(-1, head)
        headA, nextHead = head, head
        count = 0
        while nextHead:
            while nextHead and count < k:
                nextHead = nextHead.next
                count += 1
            if count == k:
                headGroup = self.reverse(headA, nextHead)
                tailGroup.next = headGroup
                tailGroup = headA
                headA = nextHead
            else:
                return dummy.next
                # headGroup = headA
            # tailGroup.next = headGroup
            # tailGroup = headA
            # headA = nextHead
            count = 0

        return dummy.next

    def reverse(self, head: Optional[ListNode], nextHead: Optional[ListNode]) -> Optional[ListNode]:
        pre, curr = nextHead, head
        while curr != nextHead:
            nxt = curr.next
            curr.next = pre
            pre = curr
            curr = nxt
        return pre
