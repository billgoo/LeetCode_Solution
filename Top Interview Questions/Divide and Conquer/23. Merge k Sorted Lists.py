# 23. Merge k Sorted Lists
# with divide and conquer
#
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


# with Priority Queue
# Java
# /**
#  * Definition for singly-linked list.
#  * public class ListNode {
#  *     int val;
#  *     ListNode next;
#  *     ListNode() {}
#  *     ListNode(int val) { this.val = val; }
#  *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
#  * }
#  */
# class Solution {
#     public ListNode mergeKLists(ListNode[] lists) {
#         if (lists.length == 0) return null;
#         // 虚拟头结点
#         ListNode dummy = new ListNode(-1);
#         ListNode p = dummy;
#         // 优先级队列，最小堆
#         PriorityQueue<ListNode> pq = new PriorityQueue<>(
#             lists.length, (a, b)->(a.val - b.val));
#         // 将 k 个链表的头结点加入最小堆
#         for (ListNode head : lists) {
#             if (head != null)
#                 pq.add(head);
#         }

#         while (!pq.isEmpty()) {
#             // 获取最小节点，接到结果链表中
#             ListNode node = pq.poll();
#             p.next = node;
#             if (node.next != null) {
#                 pq.add(node.next);
#             }
#             // p 指针不断前进
#             p = p.next;
#         }
#         return dummy.next;
#     }
# }