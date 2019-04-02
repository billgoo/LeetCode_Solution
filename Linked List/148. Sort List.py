'''
nlogn time
constant space
QuickSort approach but time limit exceeded
'''
import random

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        def getTail(l, n):
            for i in range(n - 1):
                if not l:
                    break
                l = l.next
                
            if not l:
                return None
            re = l.next
            l.next = None
            return re
        
        def merge(left, right, head):
            dummy = ListNode(float('-inf'))
            l = dummy
            while left and right:
                if left.val <= right.val:
                    l.next = left
                    left = left.next
                    l = l.next
                else:
                    l.next = right
                    right = right.next
                    l = l.next
                    
            l.next = left or right
            head.next = dummy.next
            
            while l.next:
                l = l.next
            return l
                    
        
        n = 0
        left = head
        while left:
            n += 1
            left = left.next
            
        step = 1
        dummy = ListNode(float('-inf'))
        dummy.next = head
        
        # merge sort by using divide and conquer
        while step < n:
            cur = dummy.next
            tail = dummy
            while cur:
                left = cur
                right = getTail(left, step)
                cur = getTail(right, step)
                tail = merge(left, right, tail)
            step <<= 1
        
        return dummy.next
        
        
'''
for test

if __name__ == "__main__":
    a = []
    for i in range(30000):
        a.append(random.randint(1, 100))
    # a = [2,5,3,1,4,9]
    dummy = head = ListNode(a[0])
    for i in range(1, len(a)):
        dummy.next = ListNode(a[i])
        dummy = dummy.next
    s = Solution().sortList(head)
    print(head.next.val)
    re = []
    while s != None:
        re.append(s.val)
        s = s.next
    print(re)
'''