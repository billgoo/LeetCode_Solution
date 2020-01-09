/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if (headA == null || headB == null) return null;
        
        ListNode a = new ListNode(0);
        ListNode b = new ListNode(0);
        a.next = headA;
        b.next = headB;
        
        while (a.next != b.next) {
            if (a.next != null) {
                a.next = a.next.next;
            } else {
                a.next = headB;
            }
            
            if (b.next != null) {
                b.next = b.next.next;
            } else {
                b.next = headA;
            }
        }
        
        return a.next;
    }
}