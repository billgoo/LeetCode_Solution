# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # recursive
        
        n1, n2 = self.getLength(l1), self.getLength(l2)
        
        if n1 >= n2:
            carry, new = self.addNumber(l1, l2, n1 - n2)
        else:
            carry, new = self.addNumber(l2, l1, n2 - n1)
            
        if carry:
            head = ListNode(carry)
            head.next = new
            
            return head
        
        return new
        
        
    def getLength(self, l: ListNode) -> int:
        num = 0
        while l:
            num += 1
            l = l.next
        return num
    
    
    def addNumber(self, l1: ListNode, l2: ListNode, counter: int):
        # l1 is longer than the l2
        if not l1 and not l2:
            return 0, None
        
        if counter:
            carry, new = self.addNumber(l1.next, l2, counter - 1)
            value = l1.val + carry
        else:
            carry, new = self.addNumber(l1.next, l2.next, 0)
            value = l1.val + l2.val + carry
            
        result = ListNode(value % 10)
        result.next = new
            
        return value // 10, result
            
    # 也可以用stack
