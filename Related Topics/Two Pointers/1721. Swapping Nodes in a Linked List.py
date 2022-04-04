# 1721. Swapping Nodes in a Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        head_k = ListNode(-1, head)
        tail_k = head
        tail_helper = head

        for _ in range(k):
            head_k = head_k.next
            tail_helper = tail_helper.next

        while tail_helper:
            tail_k = tail_k.next
            tail_helper = tail_helper.next

        head_k.val, tail_k.val = tail_k.val, head_k.val
        return head
