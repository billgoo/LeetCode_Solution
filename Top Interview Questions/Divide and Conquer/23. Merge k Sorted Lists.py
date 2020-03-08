# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        l = len(lists)
        if l == 0:
            return None
        elif l == 1:
            return lists[0]
        
        stack = [i for i in lists]
        while len(stack) > 1:
            left = stack.pop(0)
            right = stack.pop(0)
            stack.append(self.mergeList(left, right))
        return stack[0]
            
    def mergeList(self, left, right):
        head = ListNode(-1)
        dummy = head
        while left and right:
            if left.val > right.val:
                dummy.next = ListNode(right.val)
                right = right.next
            else:
                dummy.next = ListNode(left.val)
                left = left.next
            dummy = dummy.next
        dummy.next = left if left else right
        return head.next
                
                
            
        