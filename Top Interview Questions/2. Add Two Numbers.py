# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        dummy = root = ListNode(0)
        parent = ListNode(0)
        while l1 and l2:
            root.next = ListNode((l1.val+l2.val+root.val)//10)
            root.val = (l1.val+l2.val+root.val)%10
            parent = root
            root = root.next
            l1, l2 = l1.next, l2.next
        while l1:
            root.next = ListNode((l1.val+root.val)//10)
            root.val = (l1.val+root.val)%10
            parent = root
            root = root.next
            l1 = l1.next
        while l2:
            root.next = ListNode((l2.val+root.val)//10)
            root.val = (l2.val+root.val)%10
            parent = root
            root = root.next
            l2 = l2.next
        if root.val == 0:
            parent.next = None
        return dummy