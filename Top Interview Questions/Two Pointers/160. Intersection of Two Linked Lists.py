# 160. Intersection of Two Linked Lists
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None

        a, b = ListNode(0), ListNode(0)
        a.next, b.next = headA, headB

        while a.next != b.next:
            if a.next:
                a.next = a.next.next
            else:
                a.next = headB
            if b.next:
                b.next = b.next.next
            else:
                b.next = headA

        return a.next