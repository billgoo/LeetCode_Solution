# 21. Merge Two Sorted Lists
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        if not l1:
            return l2
        if not l2:
            return l1
        dummy = ListNode(0)
        head = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next

        head.next = l1 if l1 else l2

        return dummy.next
