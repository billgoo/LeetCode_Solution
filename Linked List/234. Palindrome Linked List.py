# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None:
            return True
        if head.next == None:
            return True
        
        n = 0
        a = head
        while a != None:
            n += 1
            a = a.next
            
        if n == 2:
            if head.val == head.next.val:
                return True
            else:
                return False
        if n == 3:
            if head.val == head.next.next.val:
                return True
            else:
                return False
            
        if n % 2:
            # odd
            mid = head
            c = 1
            while c != (n + 1) / 2:
                c += 1
                mid = mid.next
            
            pre, post = None, mid.next.next
            current = mid.next
            
            while current != None:
                post = current.next
                current.next = pre
                pre = current
                current = post
            left, right = head, pre
            while right != None:
                if left.val != right.val:
                    return False
                left = left.next
                right = right.next
            return True
        else:
            # even
            mid = head
            c = 1
            while c != n / 2:
                c += 1
                mid = mid.next
            
            pre, post = None, mid.next.next
            current = mid.next
            
            while current != None:
                post = current.next
                current.next = pre
                pre = current
                current = post
            left, right = head, pre
            while right != None:
                if left.val != right.val:
                    return False
                left = left.next
                right = right.next
            return True
            
        