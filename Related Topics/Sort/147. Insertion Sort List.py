# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        if not head:
            return head
        while head.next:
            val = head.next.val
            if head.val < val:
                head = head.next
                continue
            p = dummy
            while p.next.val < val:
                p = p.next
            temp = head.next
            head.next = head.next.next
            temp.next = p.next
            p.next = temp

        return dummy.next
